import nltk
import sys, re, os
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'onedump/'
wl = PlaintextCorpusReader(corpus_root, '.*')
print wl.words(fileids = 'Zeus.txt')

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
listtemp3

