from flask import Flask, render_template, request, url_for
from random import choice, randint
import random
import re
import pandas as pd
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from scipy import spatial
import pandas as pd
import numpy as np
import imutils
import pickle
import cv2
import os
import sys

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

path = os.path.join(SITE_ROOT, 'static/file', 'all_unique.csv')
product = pd.read_csv(open(path))

path = os.path.join(SITE_ROOT, 'static/file', 'product_probabilities_v4.csv')
prob = pd.read_csv(open(path))
prob = prob.drop(columns = ['Unnamed: 0'])
columns = str(list(product.columns))
img_url = product.img_url
product.product_name = product.product_name.fillna('')

path = os.path.join(SITE_ROOT, 'static/file', 'insta_filtered.csv')
insta = pd.read_csv(open(path))

path = os.path.join(SITE_ROOT, 'static/file', 'ins_filtered_probabilities.csv')
ins_prob = pd.read_csv(open(path))
ins_prob = ins_prob.drop(columns = ['Unnamed: 0'])
ins_url = insta.image_url

path = os.path.join(SITE_ROOT, 'static/file', 'instra_cluster_prod_max_cos.csv')
cluster = pd.read_csv(open(path))


def similarity_score(vector1,vector2):
    score = 1-spatial.distance.cosine(vector1,vector2)
    return score

def find_similar(single,image_set):
    score_vec = []
    for i in image_set:
        score_vec.append(similarity_score(single,image_set[i]))
    return score_vec

def find_product_by_url(url):
	id = ""
	try:
		id = product[product.img_url==url]['id'].tolist()[0]
	except:
		pass
	return str(id) + ".jpg"

def find_insname_by_url(url):
	id = ""
	try:
		id = insta[insta.image_url==url]['full_file_name'].tolist()[0]
	except:
		pass
	return id + ".jpg"

def similarity_df(url,n,sort_asc=False):
	try:
		img = find_product_by_url(url)
		vector = prob[img]
	except:
		img = find_insname_by_url(url)
		vector = ins_prob[img]
	sim = pd.DataFrame(columns = ['images','score'])
	sim['images'] = prob.columns.tolist()
	sim['score'] = find_similar(vector,prob)
	top_similar = sim.sort_values('score',ascending=sort_asc).head(n)
	return top_similar

def find_similar_product(image_list,category):
	info = []
	for i in image_list:
		s = re.findall("\d+",i)[0]
		url = product[product.id==int(s)][category].tolist()[0]
		info.append(url)
	return info


app = Flask(__name__)

@app.route('/')
def enter():
    return render_template('enter.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/blogger',methods = ['GET','POST'])
def blogger():
	urls = []
	bloggers = cluster.blogger.unique()
	for blogger in bloggers:
		blogger_urls = insta[insta.blogger==blogger]['image_url'].tolist()
		urls.append(random.choice(blogger_urls))
	return render_template('blogger.html', img_urls=urls, bloggers = bloggers)


@app.route('/trends/',methods = ['GET','POST'])
def trends():
	if request.method == 'POST':
		url = request.form['Id']
		blogger = insta[insta.image_url==url]['blogger'].tolist()[0]

		urls = cluster[cluster.blogger==blogger]['instra_img_url'].tolist()
		topics = cluster[cluster.blogger==blogger]['cluster'].tolist()
		likes = cluster[cluster.blogger==blogger]['instra_likes'].tolist()
		comments = cluster[cluster.blogger==blogger]['instra_comments'].tolist()
		dates = cluster[cluster.blogger==blogger]['instra_post_date'].tolist()

		return render_template('page1.html',
			img_urls=urls,
            blogger = blogger,
            topics = topics,
            likes = likes,
            comments = comments,
            dates = dates)


@app.route('/recommendation/',methods = ['GET','POST'])
def recommendation():
	if request.method=='POST':
		single_url = request.form['Id']
		
		images1 = similarity_df(single_url,6,sort_asc=False)['images'].tolist()
		scores1 = similarity_df(single_url,6,sort_asc=False)['score'].tolist()
		images2 = similarity_df(single_url,6,sort_asc=True)['images'].tolist()
		scores2 = similarity_df(single_url,6,sort_asc=True)['score'].tolist()
			
		round_scores1 = [round(score,3)*100 for score in scores1]

		urls1 = find_similar_product(images1,'img_url')
		names1 = find_similar_product(images1,'product_name')
		prices1 = find_similar_product(images1,'price')
		websites1 = find_similar_product(images1,'website')

		round_scores2 = [round(score,3)*100 for score in scores2]

		urls2 = find_similar_product(images2,'img_url')
		names2 = find_similar_product(images2,'product_name')
		prices2 = find_similar_product(images2,'price')
		websites2 = find_similar_product(images2,'website')
		return render_template('page2.html',
        img_urls1=urls1,
        scores1 = round_scores1,
        names1 = names1,
        prices1 = prices1,
        websites1 = websites1,
        img_urls2=urls2,
        scores2 = round_scores2,
        names2 = names2,
        prices2 = prices2,
        websites2 = websites2)



@app.route('/top_outfits')
def top_outfits():
	names = os.listdir(os.path.join(app.static_folder, 'images'))
	imgs = []
	for n in names:
		img_url = url_for('static', filename=os.path.join('images', n))
		imgs.append(img_url)
	return render_template('top_outfits.html', imgs=imgs)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)

