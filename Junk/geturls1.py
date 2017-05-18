import nltk
import sys, os, re
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/home/aamir/Wikipedia2Text/wikipedia2text/onedump/'
wl = PlaintextCorpusReader(corpus_root,'.*')

line = []
lines = []
article = []
article = wl.open("Zeus.txt")

for item in article.readlines():
    lines.append(item)
    

lines.sort()
rawopen = wl.raw('Zeus.txt')
lines = rawopen.splitlines()
fl = re.compile('(\[\[[^\[\[]*?\]\])')
for item in lines:
    line.append(fl.findall(item))
    

list1 = []

for item in line:
    j = str(item)
    k = j.replace('[','')
    l = k.replace(']','')
    m = l.replace('\'','')
    list1.append(m)
    

list1[1:4]
# OUT: ['Statue of Zeus at Olympia|Statue of Zeus, Olympia, Greece|Olympia, Phidias, statue, 435 BC, sculpture, Ancient Greece, 16th century, engraving', '', 'Greek language|Greek, nominative case|nominative, genitive case|genitive, Greek mythology, Mount Olympus (Mountain)|Mount Olympus, sky father|sky, List of thunder gods|thunder, thunderbolt, eagle, bull (mythology)|bull, oak, ancient Near East, scepter']
list2 = []
list3 = []
list4 = []
for item in list1:
    tempstr = str(item)
    templist = tempstr.split(',')
    for i in templist:
        list2.append(i)
        
    

list2 = filter(None, list2)
for item in list2:
    list3.append(item.lstrip())
    

for item in list3:
    list4.append(item.replace(' ','_'))
    

list4[0:40]
# OUT: ['Statue_of_Zeus_at_Olympia|Statue_of_Zeus', 'Olympia', 'Greece|Olympia', 'Phidias', 'statue', '435_BC', 'sculpture', 'Ancient_Greece', '16th_century', 'engraving', 'Greek_language|Greek', 'nominative_case|nominative', 'genitive_case|genitive', 'Greek_mythology', 'Mount_Olympus_(Mountain)|Mount_Olympus', 'sky_father|sky', 'List_of_thunder_gods|thunder', 'thunderbolt', 'eagle', 'bull_(mythology)|bull', 'oak', 'ancient_Near_East', 'scepter', 'Cronus', 'Rhea_(mythology)|Rhea', 'Hera', 'Dodona', 'Dione_(mythology)|Dione', 'Iliad', 'Aphrodite', 'Pederasty_in_ancient_Greece|pederastic_relationship', 'Ganymede_(mythology)|Ganymede', 'Athena', 'Apollo', 'Artemis', 'Hermes', 'Persephone', 'Demeter', 'Dionysus', 'Perseus']
