import nltk
import sys, re, os
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'onedump/'
wl = PlaintextCorpusReader(corpus_root, '.*')

line = []
lines = []
haha = []
haha = wl.open('Zeus.txt')

for item in haha.readlines():
    lines.append(item)
    

lines.sort()
rawopen = wl.raw('Zeus.txt')
lines = rawopen.splitlines()
fl = re.compile('(\[\[[^\[\[]*?\]\])')
for item in lines:
    line.append(fl.findall(item))
    

linefinal = []
gl = re.compile('(\[\])+')
for item in line:
    linefinal.append(gl.
    
