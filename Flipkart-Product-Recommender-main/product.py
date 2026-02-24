import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import matplotlib.pyplot as plt
import re

data=pd.read_csv(r"C:\Users\Lohesh\Downloads\Notes\Machine Learning\codes\Flask\flipkart_com-ecommerce_sample.csv")
data.fillna('',inplace=True)

data.drop_duplicates(subset=['product_name'],inplace=True)

data['text'] = data['product_category_tree'].transform(lambda s:re.sub(r'\W+', ' ', s))

data['text'] = data['text']+" "+data['product_name']+" "+data['description']+" "+data['brand']

tfidf = TfidfVectorizer(max_features=2500)
x = tfidf.fit_transform(data['text'])

def recommender(movie):
    req = x[np.where(data['product_name']==movie)[0][0]]
    score = cosine_similarity(req,x).flatten()
    ind = (-score).argsort()[1:6]
    return data['product_name'].iloc[ind]

recommender("Alisha Solid Women's Cycling Shorts")