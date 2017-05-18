import nltk, re, sys, os, urllib2
htmlstripped = []
htmlplain = []
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllink = sys.argv[1]

infile = opener.open(str.join("http://en.wikipedia.org/wiki/",                       #('http://en.wikipedia.org/wiki/Cloud_computing')
page = infile.read()
raw = nltk.clean_html(page)
pagewords = nltk.word_tokenize(raw)
 
for i in pagewords:
   j = re.sub('[^A-Za-z]+', '', i)
   htmlstripped.append(str(j))



htmlplain=filter(lambda x: len(x)>0, htmlstripped)
htmlstripped = [w for w in htmlplain if len(w) >= 4]
