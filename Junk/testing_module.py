def openurl(article):

import nltk, re, sys, os, urllib2
htmlstripped = []
htmlplain = []
infile = []

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllink = article
finalurl = 'http://en.wikipedia.org/wiki/' + urllink
infile = opener.open(finalurl)                  
page = infile.read()
raw = nltk.clean_html(page)
pagewords = nltk.word_tokenize(raw)
 
for i in pagewords:
   j = re.sub('[^A-Za-z]+', '', i)
   




for item in htmlstripped:
    if item:
        htmlplain.append(item)





htmlstripped = [w for w in htmlplain if len(w) >= 4]
