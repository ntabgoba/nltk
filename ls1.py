#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:03:49 2017

@author: ntabgoba
"""

import nltk
from nltk.book import *

for line in open("lsn.txt"):
    for word in line.split():
        if word.endswith("ing"):
            print word
        
        

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

#call the functions
percentage(text4.count("a"),len(text4))

#lists, concatenation, appending{.append},indexing&slicing {text1[173],text1[2:6]}
#strings, sliced like lists, joining {.join['monty','python']}, splitting, {'monthy python'.split()}

# 1.3 Computing with language: Simplte Stats
import pandas as pd
papers = pd.read_csv("titles_eng.csv", error_bad_lines=False)






# 2.4 Lexical Resources
# Is a collection of words and phrases with associated info such as part of speech & sense definition
#e.g if we have my_text, then vocab = sorted(set(my_text)) and word_freq = FreqDist(my_text) are simple lexical resources
#lexical entry consists of "headword" also known as "leamma" along with additional info like part of speech

# homonyms = two distinct words having the same spelling eg saw (see) and saw(4cutting)


#Example 2-3. Filtering a text: This program computes the vocabulary of a text, then removes all items that occur in an existing wordlist, leaving just the uncommon or misspelled words.
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha()) 
    english_vocab = set(w.lower() for w in nltk.corpus.words.words()) #/usr/dict/words Unix inbuilt dictionary
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)
unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))


from nltk.corpus import stopwords   #corpus of "stopwords", usually removed since, they contain no "lexical content"
stopwords.words('english')

##Let’s define a function to compute what fraction of words in a text are not in the stop- words list、
def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english') 
    content = [w for w in text if w.lower() not in stopwords] 
    return len(content) / len(text)

content_fraction(nltk.corpus.reuters.words()) 

#QUIZ
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
[w for w in wordlist if len(w) >= 4
                     and obligatory in w
                     and nltk.FreqDist(w) <= puzzle_letters]

#Another Wordlist Corpus, NAMES CORPUS 8000
names = nltk.corpus.names
names.fileids()
male_names = names.words('male.txt'); female_names = names.words('female.txt')
[w for w in male_names if w in female_names]


#PRONOUNCING DICTIONARY FROM CMU
entries = nltk.corpus.cmudict.entries()


for word, pron in entries:             #we replace entry with two var word&pron
    if len(pron) == 3:
        ph1, ph2, ph3 = pron           #assigns contents of pron to 3 new vars
        if ph1 == 'P' and ph3 == 'T':
            print word, ph2,
            

#2.WORDNET -semantically oriented dict in English similar to traditional thesaurus, 155k words, 117k synonmy sets

from nltk.corpus import wordnet as wn
wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()


#Synset -In metadata a synonym ring or synset, is a group of data elements that are considered semantically equivalent for the purposes of information retrieval 
#HYPONYMS -word with a more definite meaning like "a spoon is a hyponym of cultery".


#========================================================================
#Chapter 3 Processing Raw Text

from __future__ import division
import nltk, re, pprint
from urllib import urlopen
from bs4 import BeautifulSoup 

url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
type(raw)
len(raw)
raw[:75]
# break the string into words&punctuation
tokens = nltk.word_tokenize(raw)
type(tokens); len(tokens)
tokens[:10]
#create an nltk text
text = nltk.Text(tokens) #class = nltk.text.Text
text[1024:1060]
text.collocations()

#we manually find where the content begins and ends
raw.find("PART I") #to find index
raw.rfind("End of Project Gutenberg's Crime")  #reverse find, to get index

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
html[:60]

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
soup.find_all('a')

raw = soup.get_text()
raw[:60]

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)
text.concordance('gene')

#Processing RSS Feeds # 
import feedparser

# get out of python interpreter to terminal
import os
os.system("ls") #or os.listdir('.')


#Readling Local Files
f = open('lsn.txt','rU')  #r - open4reading, U-Universal, ignore all new line conventions
raw = f.read()  #creates a string of all the contents in f file
raw[:500]  # '\n' characters are newlines,similar to placing Enter
for line in f:
    print line.strip()  #to remove '\n' 

# Extracting Text from PDF - pypdf, MSWord - pywin32

#3.3 Text Processing with Unicode






