import nltk
import sys, re, os
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'onedump/'
wl = PlaintextCorpusReader(corpus_root, '.*')
print wl.words(fileids = 'Zeus.txt')
outfile = open('output.txt', 'w')
tempww = wl.words(fileids = 'Zeus.txt')
for i in tempww:
	j = re.sub('[^A-Za-z]+', '', i)
	outfile.write(str(j))
	outfile.write(' ')
