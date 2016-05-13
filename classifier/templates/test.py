import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
import os

os.chdir('/home/mayur/Documents/SpamKiller')
print "Hello world"
clf_multinomial = joblib.load('MultinomialNB_dump.pkl')
classification = clf_multinomial.predict(["get_first_text_block(msg_body)"])
print classification