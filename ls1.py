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

#how to use Unicode for processing texts that use non-ASCII character sets.
# Unicode supports over 1m characters, each character is assigned a number called a code point.
# in python code units are written in the form \uXXXX, where XXXX is a 4 digit hexadecimal form
#Some encodings (such as ASCII and Latin-2) use a single byte per code point,so they can support only a small subset of Unicode, enough for a single language
#Other encodings (such as UTF-8) use multiple bytes and can represent the full range of Unicode characters

# Python codecs module -functions for reading encoded data into Unicode writing strings in encoded form
import codecs
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = codecs.open(path, encoding ='latin2')


#Regular Expressions for Detecting Word Patterns
import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

[w for w in wordlist if re.search('ed$', w)]  #find words ending ed in string w, -dollar sign matches end of the word
jio = [w for w in wordlist if re.search('^..j..t..$', w)]  #get a word ..j..t..
sum(1 for w in text if re.search('^e-?mail$', w))  #? -previous character is optional, ^ -start of string, $ - end of string
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)] #words that have either of 3 chars, orderlessly

#Application of regex, -the r' makes python diff regex from normal strings
word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]', word) #finds all vowels in the word


#Finding Word Stems
def stem(word):
    for suffix in ['ing', 'ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
        return word
#We can use regex to do the above
re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

#3.6 Normalizing Text -put to lower, then stemmed (strip any affixes), -Lemmatization -put in dictionary form
# NLTK's Stemmers -PorterStemmer() and LancasterStemmer()
porter = nltk.PorterStemmer() #Good if you are indexing some texts and want to support search using alternative forms of words
lancaster = nltk.LancasterStemmer()
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
     is no basis for a system of government. Supreme executive power derives from
     a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)
[porter.stem(t) for t in tokens]

#Lemmatization -WordNet lemmatizer 
wnl = nltk.WordNetLemmatizer()  # if you want to compile the vocabulary of some texts and want a list of valid lemmas
[wnl.lemmatize(t) for t in tokens]

#3.7 Regular Expresssions for Tokenizing Text
# simple approach - split on whitespace
raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
            well without--Maybe it's always pepper that makes people hot-tempered,'..."""
re.split(r' ',raw)
re.split(r'[ \t\n]+', raw)  #matches one or more spaces i.e tabs, newlines
re.split(r'\W+', raw)  #\W split input on anything other than a word character \W = [a-zA-Z0-9]

nltk.regexp_tokenize()  # is more efficient for this task,
text = 'That U.S.A. poster-print costs $12.40..'

pattern = r'''(?x)          
    ([A-Z]\.)+          
  | \w+(-\w+)*       
  | \$?\d+(\.\d+)?%?  
  | \.\.\.            
  | [][.,;"'?():-_`]  
'''
nltk.regexp_tokenize(text, pattern)  #didnt work

#Segmentation -Sentence segemantation -word segmentation
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle') 
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents[171:181])

#3.9 Formatting: From Lists to Strings
silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']
' '.join(silly)


fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
for word in fdist:
    print word, '->', fdist[word], ';',
# dog -> 4 ; cat -> 3 ; snake -> 1 ;



#4 Writing Structured Programs
#When we assign bar = foo, it is just the object reference 3133 that gets copied
foo = ['Monty','Python']
bar = foo
foo[1] = 'Bodkin'
bar

#To copy the items from a list foo to a new list bar
bar = foo[:]  #copies the object references inside the list

#dir() Returns the attributes of the object or module.
dir(__builtins__)  # return objects in current scope i.e "__builtin__", "__doc__", "__name__" and "__package__". 
#help()	Returns the python built in documentation about the object.

#type()	    Returns the type of object.-help related to python module, object  or method

#__doc__	    Returns the doc-string of object or module.
print list.__doc__

#Conditionals
# In the condition part of an if statement, a non-empty string or list is evaluated as true, while an empty string or list evaluates as false

mixed = ['cat', '', ['dog'], []] 
for element in mixed:
    if element:
        print element
#to check whether all or any items meet some condition:
all()
any()
sent = ['No', 'good', 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '.']
all(len(w) > 4 for w in sent) #false
any(len(w) > 4 for w in sent) #true

#Sequences
#strings&lists, -Tuple -> formed with a comma operator -indexed,sliced&have length
t = 'walk','fem', 3


for item in set(s).difference(t) #Iterate over elements of s not in t
for item in random.shuffle(s) #Iterate over elements of s in random order

':'.join(words)  #convert a list of strings to a single string 

#re-arrange contents of a list
words = ['I', 'turned', 'off', 'the', 'spectroroute']
words[2], words[3], words[4] = words[3], words[4], words[2]               
                          
#zip() -zips two or more sequences together into a single list of pairs
words = ['I', 'turned', 'off', 'the', 'spectroroute']  
tags = ['noun', 'verb', 'prep', 'det', 'noun']
zip(words, tags)
#enumerate(s) - returns pairs consisting of an index and the item at that index
list(enumerate(words))                       
                          
#Combining different Sequence Types
words = 'I turned off the spectroroute'.split()    #a string is a object with methods defined in it, eg split()
wordlens = [(len(word), word) for word in words]   #use list compr to build a list of typles
wordlens.sort()                                     #sort list
' '.join(w for (_, w) in wordlens)                  #join words back into a single string

#lists -same type and arbitrary length (mutable-modifiable), tuple - different types of fixed length(immutable)

#Generator expression
max(w.lower() for w in nltk.word_tokenize(text)) #normalize and tokenize using list compr, then we get max

#STYLE
#“bible” of programming, a 2,500 page multivolume work by Donald Knuth, is called The Art of Computer Pro- gramming. 

#PROCEDURAL Vs DECLARATIVE STYLE
#Procedural -dictating machine operations step by step i.e count -keep track of tokesn seen & total-combined length of all words
tokens = nltk.corpus.brown.words(categories='news')
count = 0
total = 0
for token in tokens:
    count += 1
    total += len(token)
print total / count     #4.2765382469

#Declarative  -does same thing as above
total = sum(len(t) for t in tokens)  #generator expression to sum the token lengths
print total/len(tokens)


#FreqDist summary 
fd = nltk.FreqDist(nltk.corpus.brown.words()) 
cumulative = 0.0
for rank, word in enumerate(fd):
    cumulative += fd[word] * 100 / fd.N()
    print "%3d %6.2f%% %s" % (rank+1, cumulative, word) 
    if cumulative > 25:
        break
    
#Functions
import re
def get_text(file):
    """Read text from a file, normalizing whitespace and stripping HTML markup."""
    text = open(file).read()
    text = re.sub('\s+', ' ', text)  #strip whitespaces \s
    text = re.sub(r'<.*?>', ' ', text) #strip markpus <.*?>
    return text

#NB A python function does not require to have a return statement. 
# Some functions do a side effect - printing result, modifying a file, updating contents of a parameter to a function (such functions are called "procedures" in other prog languages)

def my_sort1(mylist):      # good: modifies its argument, no return value
    mylist.sort()
def my_sort2(mylist):       # good: doesn't touch its argument, returns value 
    return sorted(mylist)
def my_sort3(mylist):      # bad: modifies its argument and also returns it
    mylist.sort() 
    return mylist




