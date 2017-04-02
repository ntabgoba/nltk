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
titles = pd.read_csv('titles_eng.csv', sep='\t', header = 0)
titles.head()
titles.describe()
titles.tail()
from IPython.display import HTML
HTML(titles.to_html())    #R's View like in html

# How many authors
titles.columns #show columns
titles.shape  #(152115, 3)
len(titles.author.unique()) #2047 Authors
len(titles.title.unique())  #107739 Articles
# Map authors to their titles in a dictionary


# Do status on authors

#Normalize text and tokenize

#remove stop words 

#Do stats on article's words like Frequency and CumFreq


#Goal: -> Search and get closely related articles ??