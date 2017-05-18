import nltk, sys, re, os, urllib2, time, threading, Queue
from nltk import *
from nltk import metrics, stem, tokenize
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from BeautifulSoup import BeautifulSoup
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
        listtextstring = []
        textstring = " ".join(inlist)
   

        for i in inlist:
		    j = re.sub('[^A-Za-z]+', '', i)
		    templist.append(str(j))


        
        templistfinal = []
        templistfinal= self.removeEmpty(templist)
        return templistfinal



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
        filename = '/home/aamir/Wikipedia2Text/wikipedia2text/onedump/' + infilename + '.' + filetype    
        out_file = open(str(filename),'w')
        return out_file
    
#closes file taking filename and filetype as parameters and just closes it.
    def closeFile(self, infilename, filetype):
        filename = infilename + '.' + filetype
        filename.close()
        return
    
#query article from dump and get urls as list
    def getURLFromDump(self, article):
        articlelines = []
        URLlines = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []    
        corpus_root = '/home/aamir/Wikipedia2Text/wikipedia2text/onedump/'
        wl = PlaintextCorpusReader(corpus_root,'.*')
        articlename = article + '.txt'
        try:
            articletext = wl.raw(articlename)
        
        except:
            return 0
    
    
        for item in articletext.splitlines():
            articlelines.append(item)
            
        fl = re.compile('(\[\[[^\[\[]*?\]\])')
        for item in articlelines:
            URLlines.append(fl.findall(item))
        
        for item in URLlines:
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
        
        
        URLlist = []
        finalURLlist = []
        for item in list4:
            
            try:
                j = str(item)
                i = j.index('|')
                URLlist.append(item.strip('|')[0:i])
                        
 
                    
            except:
                URLlist.append(item)
            
            
            
        for item in URLlist:
            j = str(item)
            k = j.replace('"','')
            l = k.replace('*','')
            finalURLlist.append(l)
            
            
        '''for item in finalURLlist:
            s = re.sub('[Image:][a-zA-Z0-9_\.|\(\)\-]*','',str(item))
            if s:
                finalURLlist.append(s)'''
        regex = re.compile('[A-Za-z0-9]+(:)(.*)')
        finalURLlist = [x for x in finalURLlist if not regex.match(x)]       
                    
                    
                    
        return finalURLlist
    
    
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
    
    
#multithreaded python code for fetching url from a urllist sent as parameter


# utility - spawn a thread to execute target for each args
    def threadedattempt(self, urls):
        def processPage(page, url):
        # do somewthing here.
            return url, len(page)
    
        def printResults(result):
            for success, value in result:
                if success:
                    print 'Success:', value
                else:
                    print 'Failure:', value.getErrorMessage()
        
    
        
    
        def printDelta(_, start):
            delta = time.time() - start
            print 'ran in %0.3fs' % (delta,)
            return delta
    
    
    
        
    
        def fetchURLs():
            callbacks = []
            for url in urls:
                d = getPage(url)
                d.addCallback(processPage, url)
                callbacks.append(d)
       
                callbacks = defer.DeferredList(callbacks)
            callbacks.addCallback(printResults)
            return callbacks
    
        #@defer.inlineCallbacks
        
        times = []
        for x in xrange(5):
            d = fetchURLs()
            d.addCallback(printDelta, time.time())
            times.append((yield d))
        print 'avg time: %0.3fs' % (sum(times) / len(times),)


        reactor.callWhenRunning(main)
        reactor.run()


#test randomn
    def testrandom(self,urls_to_load):
        import thread,urllib
        def read_url(url):
            websites[url] = urllib.open(url).read()


        for url in urls_to_load: thread.start_new(read_url, (url,))
        while websites.keys() != urls_to_load: time.sleep(0.1)


#normalize lines
    def normalize(self, inlist):
        for item in inlist:
            stemmer = stem.PorterStemmer()
            words = tokenize.wordpunct_tokenize(item.lower().strip())


        return ' '.join([stemmer.stem(w) for w in words])


#read text from article in dump and return list of words in article
    def readTextFromDump(self, article):
        articlename = article + '.txt'
        corpus_root = '/home/aamir/Wikipedia2Text/wikipedia2text/onedump/'
        wl = PlaintextCorpusReader(corpus_root, '.*')
        allwords = wl.words(fileids = articlename)
        '''#lines = rawopen.splitlines()'''
        allwords = self.extractWordsOnly(allwords)
        return allwords
        
        
        
#extracts all external URL links from raw text and returns a list of extracted external URL's in original article
    def extractexternalURL(self, article):
        corpus_root = '/home/aamir/Wikipedia2Text/wikipedia2text/onedump/'
        wl = PlaintextCorpusReader(corpus_root, '.*')
        #tempww = wl.words(fileids = article)
        articlename = article + '.txt'
        rawopen = wl.raw(articlename)
        lines = rawopen.splitlines()
        txt = rawopen
        listfinal = []
        rg = re.compile('http..(?:\\/[\\w\\.\\-]+)+',re.IGNORECASE|re.DOTALL)
        listfinal = re.findall(rg,rawopen)
        return listfinal
