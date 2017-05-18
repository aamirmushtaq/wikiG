import nltk, sys, re, os, urllib2, time, threading, Queue
from nltk import *
from nltk.corpus import PlaintextCorpusReader, stopwords, swadesh
from twisted.internet import defer, reactor
from twisted.web.client import getPage
from ImplementedFunctions import ImplementedFunctions

myfunctions = ImplementedFunctions()
xyz = myfunctions.readTextFromDump("Zeus")
stoppedxyz = myfunctions.removeStopwords(xyz)
stoppedxyz = [w for w in stoppedxyz if len(w)>2]
fdist1 = FreqDist(stoppedxyz)
vocab = fdist1.keys()
dictkeywords = {}
for item in set(stoppedxyz):
    dictkeywords[item] = fdist1[item]
    

URLlist = myfunctions.getURLFromDump("Zeus")
urlkeywordmap = {}
for item in set(stoppedxyz):
    for url in URLlist:
        if item in url:
            urlkeywordmap[url] = item
            
        
    

urlkeywordmap
# OUT: {'Tartarus': 'art', 'chariot': 'chariot', 'chthonic': 'chthonic', 'Balkan_mountains': 'mountains', 'Echo_(mythology)': 'myth', 'Charites': 'rite', 'Sabazius': 'ziu', 'Melpomene': 'men', 'Cult_(religion)': 'religion', 'Old_High_German_language': 'language', 'Europa_(mythology)': 'myth', 'Proto-Indo-European_religion': 'religion', 'death': 'death', 'Titan_(mythology)': 'myth', 'Io_(mythology)': 'myth', 'retinue': 'retinue', 'Hera': 'era', '(including_Pelops_and_Poseidon_episode)': 'including', 'Nike_(mythology)': 'myth', 'Epimenides': 'men', 'Chaos_(mythology)': 'myth', 'Alcmene': 'men', 'ancient_Near_East': 'ancient', 'Dike_(goddess)': 'goddess', 'Lycaon_(mythology)': 'myth', 'Rhea_(mythology)': 'myth', 'Limos_(mythology)': 'myth', 'Jupiter_(god)': 'god', 'Perseus_(mythology)': 'myth', 'modification': 'modification', 'Leda_(mythology)': 'myth', 'Heracles': 'era', 'Britomartis': 'art', 'Palaikastro': 'ast', 'heaven': 'heaven', 'William_Smith_(lexicographer)': 'lexicographer', 'Amalthea_(mythology)': 'myth', 'lightning': 'lightning', 'Elara_(mythology)': 'myth', 'tiwaz': 'tiwaz', 'Germanic_tribes': 'tribes', 'Maia_(mythology)': 'myth', 'Epirus_(region)': 'region', 'Thebe_(mythology)': 'myth', 'List_of_thunder_gods': 'und', 'DotA_Allstars': 'stars', 'Aegina_(mythology)': 'myth', 'Catasterismi': 'eris', 'Phidias': 'hid', 'Nyx_(mythology)': 'myth', 'archetype': 'archetype', 'emetic': 'emetic', 'daimon': 'daimon', 'thunder': 'und', 'paideia': 'paideia', 'religion': 'religion', 'Hebe_(mythology)': 'myth', 'Pederasty_in_ancient_Greece': 'ancient', 'eagle': 'eagle', 'Ganymede_(mythology)': 'myth', 'hero': 'hero', 'monster': 'monster', 'ephebe': 'ephebe', 'Egyptian_mythology': 'myth', 'Greek_mythology': 'myth', 'bronze': 'bronze', 'engraving': 'engraving', 'goddess': 'goddess', 'scepter': 'scepter', 'cornucopia': 'cornucopia', 'Pollux_(mythology)': 'myth', 'Lachesis': 'hes', 'Pausanias_(geographer)': 'geographer', 'Echidna_(mythology)': 'myth', 'nymph': 'nymph', 'Chelone_(Greek_mythology)': 'myth', 'Jupiter_(mythology)': 'myth', 'Euphrosyne_(mythology)': 'myth', 'Roman_mythology': 'myth', 'genitive_case': 'case', 'nominative_case': 'nominative', 'Norse_mythology': 'myth', 'Hercules_(1997_film)': 'film', 'Fates': 'ate', 'Euterpe_(mythology)': 'myth', 'quadrennial': 'quadrennial', 'bull_(mythology)': 'myth', 'peleiades': 'peleiades', 'Ananke_(mythology)': 'myth', 'Megalopolis': 'polis', 'festival': 'festival', 'Orestes': 'rest', 'Sparta': 'art', 'Eris_(mythology)': 'myth', 'interpretatio_graeca': 'graeca', 'Polyhymnia': 'hymn', 'cannibalism': 'cannibalism', 'Dione_(mythology)': 'myth', 'stomach': 'stomach', 'Zethus': 'thus', 'rite_of_passage': 'rite', 'Taygete': 'get', 'Castor_and_Polydeuces': 'ast', 'Greek_temple': 'temple', 'Penthus': 'thus', 'Harpies': 'pie', 'agora': 'agora', 'sculpture': 'sculpture', 'Robert_Graves': 'ves', 'Etruscan_mythology': 'myth', 'Lamia_(mythology)': 'myth', 'vocative': 'vocative', '16th_century': 'century', 'mountain': 'mount', 'Nemesis_(mythology)': 'myth', 'oak': 'oak', 'read_by_Timothy_Carter': 'art', 'polis': 'polis', 'Carme_(mythology)': 'myth', 'goat': 'goat', 'Gaia_(mythology)': 'myth', 'thunderbolt': 'und', 'Himalia_(mythology)': 'myth', 'epithet': 'epithet', 'Metis_(mythology)': 'myth', 'Rhodope_mountains': 'mountains', 'statue': 'statue', 'Incubation_(ritual)': 'ritual', 'Astraea_(mythology)': 'myth', 'Callisto_the_Greek_myth': 'myth', 'Maera': 'era', 'Agamemnon': 'game', 'werewolf': 'werewolf', 'Thebes': 'hebe', 'Bia_(mythology)': 'myth', 'Germanic_mythology': 'myth', 'Earth': 'art', 'Greek_language': 'language', 'Xanthus': 'thus'}
