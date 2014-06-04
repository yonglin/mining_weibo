# -*- coding: utf-8 -*-
from __future__ import  division
import nltk
from nltk.corpus import movie_reviews
import collections
import nltk.metrics
from nltk.corpus import stopwords
from nltk.stem import *
from nltk.stem.porter import *

import random
import re
import pickle
import json
from numpy import percentile

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm

import urllib2
"""
Login to Sina Weibo with cookie
"""

COOKIE = 'SINAGLOBAL=9412320484407.246.1391513353463; YF-Ugrow-G0=69bfe9ce876ec10bd6de7dcebfb6883e; YF-V5-G0=7c921c6e0c6c1cca0ae70cdcfe506e27; _s_tentry=www.weibo.com; Apache=600201312918.216.1401849048135; ULV=1401849048227:161:5:5:600201312918.216.1401849048135:1401837349019; YF-Page-G0=324e50a7d7f9947b6aaff9cb1680413f; myuid=2123618881; login_sid_t=426b2eb52cc70f5c959fd2ae99fdd366; UOR=,,login.sina.com.cn; SUS=SID-2123618881-1401849098-GZ-e9nix-8c1cc15f501deca852e37ca09718208b; SUE=es%3D59faf1bc302229c2f5f4b3ed43fe3a54%26ev%3Dv1%26es2%3Dcab7d37ebdf36bd8c87ca3150ed5dfac%26rs0%3DeBYXkBt7fpuR%252Fcz6JPFWbhsXBNY91s%252BAHmVcAQOF7%252Fup5UnjVSB0IgsFbigKLi0AjlinZLfO3Sll833sYnXuUn1XgH4V6qAhZeVBw6KT%252FTMke7AJF9qzGvjrEFCSbst40FYbTPfyCR7zEJ0x9pekKxaTrEDIkszLlxkKKvyc1YE%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1401849098%26et%3D1401935498%26d%3Dc909%26i%3D208b%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2123618881%26name%3Dzhuoylin%2540live.cn%26nick%3Dzhuoylin%26fmp%3D%26lcp%3D2012-12-06%252022%253A57%253A00; SUB=AbMfKSi0tdM6qrAqGHQgb0ZrPBpZWxlZ3nQoKfSP4BBdWMTTBBuOXQnDRxYXnv%2FnSW%2BhJLiFEI8%2BYgKtMoiYhr1TaoUvnCs1fe%2Fko5qIXOGJvTXkWYt3HYdgiFo4R9lsPWJ3Ug6gLMsiVi3Cadv9f5Y%3D; SUBP=002A2c-gVlwEm1uAWxfgXELuuu1xVxBxAAkT5EE38JjiTCzTR4yTQU2uHY-u_1%3D; ALF=1433385098; SSOLoginState=1401849098; un=zhuoylin@live.cn; wvr=5'

#fill with your weibo.com cookie
HEADERS = {"cookie": COOKIE}

def get_page(url):
    #url = 'http://s.weibo.com/wb/%E5%BC%A0%E5%8D%83%E5%B8%86&xsort=hot'
    req = urllib2.Request(url, headers=HEADERS)
    r = urllib2.urlopen(req)
    web_page = r.read()
    #desc = nltk.clean_html(text)
    print "1"
    return web_page
    #pat_title = re.compile('<title>(.+?)</title>')
    #r = pat_title.search(text)
    #if r:
        #print r.group(1)

def get_regular_content(str, rule):
  regular_content = re.findall(rule, str)
  return regular_content

def get_weibo_unicode(url):

  rule=r'feed_list_content.*?<\\/div>\\n'
  page = get_page(url)
  weibos = get_regular_content(page,rule)
  weibo = ''.join(weibos)
  weibo_json = '"'+weibo+'"'
  weibo_unicode = json.loads(weibo_json)
  return weibo_unicode

def wash_CN(url):
  weibo = get_weibo_unicode(url)
  rule_C = "[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\@\#\\\&\*\%\"\ \_\-\。\，\①\》\《\\n\！]"
  clean_weibo = re.sub(rule_C,"",weibo)
  return clean_weibo


def keep_data(address,raw_data):
  '''using pickle to store the raw data'''

  filename = address
  data = raw_data
  f = open(filename, 'wb')
  pickle.dump(data, f) # dump the object to a file
  f.close()

def get_data(address):
  '''using pickle to get the raw data'''

  f = open(address, 'rb')
  data = pickle.load(f) # load the object from the file
  f.close()
  return data


def wash_data(desc):
  '''input a list of strings
  output a list of washed strings'''
  import jieba
  seg_list = jieba.cut(desc, cut_all=False)
  return ' '.join(seg_list)

data_set = lw+rw
desc = [(wash_data(item[0]), item[1]) for item in data_set]
corpus_moive = [d for (d,c) in desc]
  ## CountVectorizer can autmatically deal with the counting stuff 
vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus_moive)
############

########## change 'pos' and 'neg' into 1 and 0, respectively
Y = [item[1] for item in desc]

#http://scikit-learn.org/stable/modules/feature_extraction.html

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
  ## get the tfidf matrix
X_train = tfidf[0:140,]
y_train = Y[0:140]
#test_set = L1[0:1600]
X_test= tfidf[140:,]
y_test = Y[140:]
#y_train = 


#http://scikit-learn.org/stable/modules/svm.html

C = 1  # SVM regularization parameter
#clf = svm.SVC()
#clf.fit(X_train, y_train) 

svc = svm.SVC(kernel='linear', C=C).fit(X_train, y_train) 
  ## linear kernel is not so~~~~o good
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X_train, y_train) 
  ## linear kernel can get a good result
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X_train, y_train) 
  ## poly kernel is not so~~~~o good
lin_svc = svm.LinearSVC(C=C).fit(X_train, y_train) 
  ## LinearSVC  can get the best result

  ## train a classifier by using the train_set
refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)


for i, item in enumerate(y_test):
  refsets[item].add(i)

  observed = lin_svc.predict(X_test[i,])
  testsets[observed[0]].add(i)

print 'Results of Prediction:\n' 
print 'lin_svc Right Wing precision:', nltk.metrics.precision(refsets[1], testsets[1])
print 'lin_svc Right Wing recall:', nltk.metrics.recall(refsets[1], testsets[1])
print 'lin_svc Right Wing F-measure:', nltk.metrics.f_measure(refsets[1], testsets[1])
print 'lin_svc Left Wing precision:', nltk.metrics.precision(refsets[0], testsets[0])
print 'lin_svc Left Wing recall:', nltk.metrics.recall(refsets[0], testsets[0])
print 'lin_svc Left Wing F-measure:', nltk.metrics.f_measure(refsets[0], testsets[0])
print 'lin_svc accuracy:', nltk.metrics.scores.accuracy(refsets, testsets)
print '\n'

