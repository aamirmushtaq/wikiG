import nltk
import sys, re, os
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'onedump/'
wl = PlaintextCorpusReader(corpus_root, '.*')
outfile = open('output.txt', 'w')
tempww = wl.words(fileids = 'Zeus.txt')
listtemp = []
for i in tempww:
   j = re.sub('[^A-Za-z]+', '', i)
   listtemp.append(str(j))

listtemp1 = []
listtemp2 = []
listtemp3 = []
listtemp3=filter(lambda x: len(x)>0, listtemp)
listtemp2 = sorted(set(listtemp3))
for item in listtemp2:
   listtemp1.append(listtemp3.count(item))
   

fdist = nltk.FreqDist(listtemp3)
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
listtemp4 = []
for words in stop_words:
   while words in listtemp3:
       listtemp3.remove(words)
       
   

for items in listtemp3:
   listtemp4.append(items.lower())
   

for words in stop_words:
   while words in listtemp4:
       listtemp4.remove(words)


listfinal = []
listfinal = [w for w in listtemp4 if len(w) >= 4]
len(listfinal)
len(set(listfinal))
