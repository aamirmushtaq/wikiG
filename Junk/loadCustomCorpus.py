import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'Wikipedia2Text/wikipedia2text/outtemp/'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
wordlists.words('ff/f7/Meta-ethics.txt')
