import nltk
import sys, re, os
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh

class MyNLTK:
	
	def extractWords(self, list1):
		templist = []
		for i in list1:
			j = re.sub('[^A-Za-z]+', '', i)
			templist.append(str(j))
		
		return templist
		
	def removeEmpty(self, list1):
		return filter(lambda x: len(x)>0, list1)
		
	def sortedSet(self, list1):
		return sorted(set(list1))
		
	def copyLists(self, list1):
		list2 = []
		for item in list1:
			list2.append(item)
			
		return list2
		
	def removeStopwords(self, list1, stop_words):
		templist = self.copyLists(list1)
		for words in stop_words:
			while words in templist:
				templist.remove(words)
				
		return templist
