import sys, os, re
import nltk
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from my_nltk_funs import MyNLTK

class MyBegin:
	def __init__(self):
		self.corpus_root = sys.argv[1]
		self.fileID = sys.argv[2]
		self.my_corpus = PlaintextCorpusReader(self.corpus_root, '.*')
		self.my_article = self.my_corpus.words(fileids = self.fileID)
		
def main():
	starts = MyBegin()
	nltk_funs = MyNLTK()
	
	list_of_words = []
	list_sorted_set = []
	list_keywords1 = []
	
	list_of_words = nltk_funs.extractWords(starts.my_article)
	list_of_words = nltk_funs.removeEmpty(starts.my_article)
	
	list_sorted_set = nltk_funs.sortedSet(starts.my_article)
	
	stop_words1 = stopwords.words('english')
	stop_words2 = swadesh.words('en')
	
	list_keywords1 = nltk_funs.removeStopwords(list_of_words, stop_words1)
	list_keywords2 = nltk_funs.removeStopwords(list_keywords1, stop_words2)
	
#	for i in list_of_words:
#		print i	
	
	print len(list_of_words)
	print len(list_sorted_set)
	print len(list_keywords1)
	print len(list_keywords2)
		

if __name__ == '__main__':
	main()
