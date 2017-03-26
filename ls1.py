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

#generate random text
text2.generate()

#token - technical name for a sequence of characters eg hair,:,his, that we want to treat as a group
len(text3) #number of words in entire text

#tokens in "to be or not to be" are "2to, 2be,1or,1not"
#However, a set of above tokens, all duplicates wil be collapsed/removed

len(sorted(set(text3)))
# 2789 word types, - form or spelling of word independent of its specific occurences in a text

#to calculate lexical richness of the text
from __future__ import division
len(text3)/len(set(text3))
#16.05, each word is used 16 times on average.

#how often a word occurs in a text
text3.count("smote")
text5.count("lol")
100*text5.count("lol")/len(text5)

#write a function that does the above
def lexical_diversity(text):
    return len(text)/len(set(text))
def percentage(count, total):
    return 100*count/total