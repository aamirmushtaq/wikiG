import nltk, sys, re, os, urllib2, threading, time, 
from nltk import *
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
import ImplementedFunctions
from ImplementedFunctions import ImplementedFunctions
myFunctions = ImplementedFunctions()

urls = ['http://www.google.com/','http://www.lycos.com/','http://www.bing.com/','http://www.altavista.com/','http://achewood.com/']
myFunctions.threadedattempt(urls)
myFunctions.getFromDump('Zeus')





















import nltk, sys, re, os, urllib2, time, threading, Queue
from nltk import *
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from ImplementedFunctions import ImplementedFunctions

myfunctions = ImplementedFunctions()
myfunctions.readFilesNameList("/home/aamir/Wikipedia2Text/wikipedia2text/onedump/")

allfilenames = myfunctions.readFilesNameList("/home/aamir/Wikipedia2Text/wikipedia2text/onedump/")
filenames = []
for item in allfilenames:
    filenames.append(item.replace("/home/aamir/Wikipedia2Text/wikipedia2text/onedump/",""))
    

articlenames = []
for item in filenames:
    articlenames.append(item.replace(".txt",""))
    






for item in articlenames:
    filewrite_url = myfunctions.openforwrite(item,'urls')
    filewrite_keywords = myfunctions.openforwrite(item,'keywords')
    urllist = []    
    urllist = myfunctions.getURLFromDump(item)
    filewrite_url.write(urllist)
    
