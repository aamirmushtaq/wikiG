import nltk, sys, re, os, urllib2
from nltk import *
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh


class ImplementedFunctions:
#opens an article from article name via net. costly and only called if article not available in dump
    def openUrlArticle(self, article):
    
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
        '''for i in pagewords:
            j = re.sub('[^A-Za-z]+', '', i)
            htmlstripped.append(str(j))                                     #this block of code removes all non alphachars and empty items so ignored as functions are made for the purpose
        
        for item in htmlstripped:
            if item:
                htmlplain.append(item)
            
        '''    
        htmlstripped = [w for w in pagewords if len(w)>4]
        return htmlstripped
    

    #extract words from the list ignoring all non alphabets returning a list of only words and no digits
    def extractWordsOnly(self, inlist):
        templist = []
        for i in inlist:
		    j = re.sub('[^A-Za-z]+', '', i)
		    templist.append(str(j))


        return templist



    #removes the stopwords from the list and returns refined list  NOTE: also converts the list to lowercase
    def removeStopwords(self, inlist):
        stop_words1 = stopwords.words('english')
        stop_words2 = swadesh.words('en')
        finalstopwords = stop_words1 + stop_words2
        templist = []
        for items in inlist:
            templist.append(items.lower())
    
    
    	for words in finalstopwords:
    		while words in templist:
    			templist.remove(words)
    
    			
    	return templist
    
    
    #reads all filenames and returns a list of all files with path from current directory so that one can access it.
    
    def readFilesNameList(self, path):
        basePath = path
        allfiles = []
        subfiles = []
        for root, dirs, files in os.walk(basePath):
          for f in files:
             if f.endswith('.txt'):
                 allfiles.append(os.path.join(root,f))
                 if root!=basePath:
                     subfiles.append(os.path.join(root, f))
      
    
                  
                
        return allfiles
    
    #get the frequency distribution of the list after extraction.
    def getFreqDist(self, inlist):
        fdist = nltk.FreqDist(inlist)
        return fdist
    
    
    
    #remove empty items from list and returns a list that contains no empty items
    def removeEmpty(self, inlist):
        templist = []
        for item in inlist:
            if item:
                templist.append(item)
    
    
        return templist
    
    
    #sort a list return sorted list
    def sortList(self, inlist):
        return sorted(inlist)
    
    #open a file for writing with filename as parameter and now we can use functions such as write, close etc.
    def openforwrite(self, infilename, filetype):
        filename = infilename + '.' + filetype    
        out_file = open(str(filename),'w')
        return out_file
    
    #closes file taking filename and filetype as parameters and just closes it.
    def closeFile(self, infilename, filetype):
        filename = infilename + '.' + filetype
        filename.close()
        return
    
    #query article from dump
    def getFromDump(self, article):
        articlelines = []
        URLlines = []
        list1, list2,list3, list4 = []    
        corpus_root = 'the_dump/'
        wl = PlaintextCorpusReader(corpus_root,'.*')
        articlename = article + '.txt'
        try:
            articletext = wl.raw(articlename)
        
        except:
            return 0
    
    
        for item in articletext.splitlines():
            articlelines.append(item)
            
        fl = re.compile('(\[\[[^\[\[]*?\]\])')
        for item in lines:
            URLlines.append(fl.findall(item))
        
        for item in line:
            j = str(item)
            k = j.replace('[','')
            l = k.replace(']','')                                   #sample List1 = ['Statue of Zeus at Olympia|Statue of Zeus, Olympia, Greece|Olympia, Phidias, statue, 435 BC, sculpture, Ancient Greece']
            m = l.replace('\'','')
            list1.append(m)
    
        #split the list1 at comma to atomize list
        for item in list1:
            tempstr = str(item)
            templist = tempstr.split(',')
            for i in templist:
                if i:
                    list2.append(i)
    
    
        #remove starting whitespaces    
        for item in list2:
            list3.append(item.lstrip())
        
        #replace whitespace with _ to query easily from wikipedia.org
        for item in list3:
            list4.append(item.replace(' ','_'))
        
        
        URLlist = list4
        return URLlist
    
    
    #get the top n elements from list
    def getTopElements(self, inlist, n):
        return inlist[0:n]
    
    #get range of elements from list
    def getElementRange(self, inlist, x, y):
        return inlist[x:y]
    
    #get the bottom n elements from list
    def getBottomElements(self, inlist, n):
        i = len(inlist)
        j = i - n
        return inlist[j:]
    
    
    #return sorted  
