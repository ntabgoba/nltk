#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:03:49 2017

@author: ntabgoba
"""

for line in open("lsn.txt"):
    for word in line.split():
        if word.endswith("ing"):
            print word
        
        
from nltk.book import *
texts() #list texts
text1.concordance("monstrous") #show monstrous and neighboring texts
text3.concordance("lived")
text4.concordance("terror")

#what other words that appear in a similar range of contexts

text1.similar("monstrous")
text2.similar("monstrous")

#to examine contexts tahta are shared by tow or more words
text2.common_contexts(["monstrous","very"])
text3.common_contexts(["life","God"])

#dispersion plot -positional information of a word in a text
text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])