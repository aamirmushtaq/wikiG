import nltk, sys, re, os, urllib2, time, threading, Queue
from nltk import *
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from ImplementedFunctions import ImplementedFunctions

myfunctions = ImplementedFunctions()
exturllist = myfunctions.extractexternalURL("Zeus")
articlename = 'Zeus' + '.txt'
corpus_root = '/home/aamir/Wikipedia2Text/wikipedia2text/onedump/'
wl = PlaintextCorpusReader(corpus_root, '.*')
rawopen = wl.raw(articlename)
for item in exturllist:
    rawopen = rawopen.replace(item,'')
    



outfile = open("tempsadsaaaaaaa.txt",'w')
for item in rawopen:
    outfile.write(item)
    

outfile.close()
