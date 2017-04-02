#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:42:29 2017

@author: ntabgoba
"""

import pandas as pd
import re
import matplotlib as plt
os.getcwd()
os.chdir('/Users/ntabgoba/nltk1/')
df = pd.read_csv('titles_eng.csv', sep='\t', header = 0)
df.head()
df.describe()
df.tail()
from IPython.display import HTML
HTML(df.to_html())    #R's View like in html

# How many authors
df.columns #show columns
df.shape  #(152115, 3)
len(df.author.unique()) #2047 Authors
len(df.title.unique())  #107739 Articles
df.author.describe() #top 村田　正幸, #freq  972

#replace Japanese names with numbers! or learn to handle jp and eng
df['author'] = np.where(df['author'] == japense, df['sentence_id']),df['author'])

# Map authors to their df in a dictionary
corpus =  dict(zip(df.author,df.title)) 
type(corpus)
corpus.items()

                 
# Do statss on authors

#Normalize text and tokenize

#Remove stop words 

#Do stats on article's words like Frequency and CumFreq

#Stemming and Lemmatization of titles

#Goal: -> Search and get closely related articles ??
#-if author is search, bring their other articles or his/her co-authors
#-titles -bring similar words
#-