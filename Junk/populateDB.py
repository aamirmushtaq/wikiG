import nltk, sys, re, os, urllib2, time, threading, Queue, pymongo, operator
from nltk import *
from nltk import metrics, stem, tokenize
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from BeautifulSoup import BeautifulSoup
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from testImplemented import testImplemented

myfunctions = testImplemented()
allfilenames = myfunctions.readFilesNameList("/home/aamir/code/onedump/")
filenames = []
for item in allfilenames:
    filenames.append(item.replace("/home/aamir/code/onedump/",""))
    

articlenames = []
for item in filenames:
    articlenames.append(item.replace(".txt",""))
    

wordlist = []
keywordCountDict = dict()
for item in articlenames:
    wordlist = myfunctions.readTextFromDump(item)
    wordlist = myfunctions.removeEmpty(wordlist)
    wordlist = myfunctions.removeStopwords(wordlist)
    keywordCountDict = myfunctions.makedict_keyword(wordlist)
    sortedkeywordCountDict = myfunctions.decrSortDictOnValue(keywordCountDict)
    myfunctions.insKeywordCountinDB(sortedkeywordCountDict, 'tempdb', item)
    
'''  
import nltk, sys, re, os, urllib2, time, threading, Queue, pymongo, operator
from nltk import *
from nltk import metrics, stem, tokenize
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from BeautifulSoup import BeautifulSoup
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from testImplemented import testImplemented
myfunctions = testImplemented()
wordlist = myfunctions.readTextFromDump("Zeus")
wordlist = myfunctions.removeEmpty(wordlist)
wordlist = myfunctions.removeStopwords(wordlist)
keywordCountDict = myfunctions.makedict_keyword(wordlist)
sortedkeywordCountDict = myfunctions.decrSortDictOnValue(keywordCountDict)
myfunctions.insKeywordCountinDB(sortedkeywordCountDict, 'newdb', 'Zeus')
'''
