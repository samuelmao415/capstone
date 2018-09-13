import numpy as np
from scipy import spatial
import pandas as pd
import re
from gensim.utils import simple_preprocess



def calcAvg(s, tfidf_dict, avgVec = True):

	words = simple_preprocess(s)
	embedding_vector = np.zeros(len(words))
	i = 0
	for word in words:
		embedding_word = tfidf_dict.get(word)
		if embedding_word is not None:
			# Words not found in embedding index will be all-zeros.
			embedding_vector[i] = embedding_word
		i+=1


def similarity_score(df, i, j, tfidf_dict):
	vec1 = calcAvg(df.iloc[i,0], tfidf_dict)
	vec2 = calcAvg(df.iloc[j,0], tfidf_dict)

	score = 1-spatial.distance.cosine(vec1,vec2)
	return score


def find_similar(df, i, tfidf_dict, count = 10):
	score_dic = {}
	for j in range(0, df.shape[0]):
		score_dic[j] = similarity_score(df,i,j, tfidf_dict)
	sorted_by_value = sorted(score_dic.items(), key=lambda kv: kv[1], reverse = True)
	return sorted_by_value[0:count]
