import nltk
import sys, re, os
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'onedump/'
wl = PlaintextCorpusReader(corpus_root, '.*')
outfile = open('output.txt', 'w')
tempww = wl.words(fileids = 'Berlin.txt')
rawopen = wl.raw('Berlin.txt')
lines = rawopen.splitlines()
txt = rawopen

re1='(http)'# Variable Name 1
re2='(.)'# Any Single Character 1
re3='(.)'# Any Single Character 2
re4='((?:\\/[\\w\\.\\-]+)+)'# Unix Path 1

rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    var1=m.group(1)
    c1=m.group(2)
    c2=m.group(3)
    unixpath1=m.group(4)
    print var1+c1+c2+unixpath1
    


rg = re.compile('http..(?:\\/[\\w\\.\\-]+)+',re.IGNORECASE|re.DOTALL)
re.findall(rg,rawopen)
