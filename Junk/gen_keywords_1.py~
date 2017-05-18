import nltk
import sys, re, os
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh

#give path to your corpus
corpus_root = 'onedump/'
wl = PlaintextCorpusReader(corpus_root, '.*')

#select a sample article from the corpora to work on
tempww = wl.words(fileids = 'Zeus.txt')
listtemp = []

#using regular expression, eliminate everything except words (and spaces) and store in list
for i in tempww:
  j = re.sub('[^A-Za-z]+', '', i)
  listtemp.append(str(j))

#some lists to work with
listtemp1 = []
listtemp2 = []
listtemp3 = []
listtemp4 = []

#listtemp1 contains set of all words, here empty elements of list are removed
listtemp1 = filter(lambda x: len(x)>0, listtemp)

#listtemp2 contains set of sorted words from listtemp1
listtemp2 = sorted(set(listtemp1))


#now eliminate english stopwords
stop_words1 = stopwords.words('english')
#items in listtemp2 copied to listtemp3 
for items in listtemp1:
    listtemp3.append(items.lower())
    

for words in stop_words1:
    while words in listtemp3:
        listtemp3.remove(words)
        

#copy items from listtemp3 to listtemp4
for items in listtemp3:
    listtemp4.append(items)
    


#now eliminate swadesh words
stop_words2 = swadesh.words('en')
for words in stop_words2:
    while words in listtemp4:
        listtemp4.remove(words)
        
    


#create a final list
finallist1 = []

#eliminate all words with 3 or less characters
finallist1 = [w for w in listtemp4 if len(w) >= 4]

#sort the final list
finallist1 = sorted(finallist1)

#take frequency distribution of the final list
freq1 = nltk.FreqDist(finallist1)
vocab = freq1.keys()
#select top 'n' frequently occuring words
vocab[:30]
# OUT: ['zeus', 'mythology', 'greek', 'gods', 'hera', 'http', 'also', 'html', 'cronus', 'category', 'children', 'greece', 'jupiter', 'oracle', 'ancient', 'dictionary', 'dione', 'gaia', 'olympia', 'raised', 'religion', 'smith', 'title', 'first', 'mount', 'nowiki', 'pausanias', 'roman', 'statue', 'temple']

#code to write these top 'n' words into a file
nodes = []
nodes = set(vocab[:30])
out_file = open('output1.txt','w')
for items in nodes:
    out_file.write(items)
    out_file.write('\n')
    

out_file.close()
