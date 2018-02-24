# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:10:27 2018

@author: Kranthi
"""
import sys
sys.stdout=open("two.txt","w")
import re
#initialize stopWords
stopWords = []
#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end
def processTweet(tweet):
    # process the tweets
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to link
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','link',tweet)
    #Convert @username to user
    tweet = re.sub('@[^\s]+','user',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet    
#start getStopWordList
def getStopWordList(stopwords):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('user')
    stopWords.append('url')
    fp = open(stopwords, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end
#start getfeatureVector
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end
#Read the tweets one by one and process it
fp = open('prcsdtws.txt', 'r')
line = fp.readline()
st = open('prcsdtws.txt', 'r')
stopWords = getStopWordList('stopwords.txt')
while line:
    processedTweet = processTweet(line)
    featureVector = getFeatureVector(processedTweet)
    print (featureVector)
    line = fp.readline()
#end loop
fp.close()
sys.stdout.close()

