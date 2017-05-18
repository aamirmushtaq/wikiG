import nltk, sys, re, os, urllib2, time, threading, Queue, pymongo, operator, json, uuid, simplejson
from nltk import *
from nltk import metrics, stem, tokenize
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from BeautifulSoup import BeautifulSoup
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from testImplemented import testImplemented
from flask import Flask, render_template, request

app = Flask(__name__)
#DBName = 'newdb'
DBName = 'tempdb'
myfunctions = testImplemented()
#global tempVar

@app.route("/")
def start():
    return render_template('demo2.html')


@app.route("/returnjson/<name>")
def returnjson(name):
    #tempVar = request.form['articlename']
    #JSONstring = myfunctions.makeJSON(DBName,tempVar)
    JSONstring = myfunctions.makeJSON2(DBName,str(name))
    #print name
    return JSONstring


if __name__ == "__main__":
    app.run(debug=True)
