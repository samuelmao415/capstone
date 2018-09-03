from flask import Flask, render_template, request, url_for
from random import choice
import os

app = Flask(__name__)

@app.route('/')
def showImg():	
	names = os.listdir(os.path.join(app.static_folder, 'images'))

##############This will random choose one image to display ##################

	img_url = url_for('static', filename=os.path.join('images', choice(names)))
	return render_template('simple_image.html', img_url=img_url)

###############This will list all the images in the subfolder ###########################
#	imgs = []
#	for n in names:
#		img_url = url_for('static', filename=os.path.join('images', n))
#		imgs.append(img_url)
#	return render_template('all_images.html', img_urls=imgs)
