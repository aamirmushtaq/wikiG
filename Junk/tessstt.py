import nltk, sys, re, os, urllib2, time, threading, Queue
from nltk import *
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from ImplementedFunctions import ImplementedFunctions

myfunctions = ImplementedFunctions()


allfilenames = myfunctions.readFilesNameList("/home/aamir/Wikipedia2Text/wikipedia2text/onedump/")
filenames = []
for item in allfilenames:
    filenames.append(item.replace("/home/aamir/Wikipedia2Text/wikipedia2text/onedump/",""))
    

articlenames = []
for item in filenames:
    articlenames.append(item.replace(".txt",""))
    


for item in articlenames:
    filewrite_url = myfunctions.openforwrite(item,'urls')
    urllist = []    
    urllist = myfunctions.getURLFromDump(item)
    for url in urllist: 
        filewrite_url.write(url + '\n')
        
        
        
    filewrite_url.close()
    

