# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 16:51:14 2018

@author: Kranthi
"""
#import stopwords
import nltk
import csv
import sys
sys.stdout=open("three.txt","w")
import re
nltk.download()
from nltk.corpus import stopwords
stopwords.words('english')
#Read the tweets one by one and process it
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
inpTweets = csv.reader(open('tweets.csv', 'rb'), delimiter=',', quotechar='|')
tweets = [(['hey', 'cici', 'luv', 'mixtape', 'drop', 'soon', 'fantasy', 'ride'], 'positive'),
           (['heard', 'congrats'], 'positive'),
           (['ncaa', 'franklin', 'wild'], 'positive'),
           (['share', 'jokes', 'quotes', 'music', 'photos', 'news', 'articles', 'facebook', 'twitter'], 'neutral'),
           (['night', 'twitter', 'thelegionofthefallen', 'cimes', 'awfully'], 'neutral'),
           (['finished', 'mi', 'run', 'pace', 'gps', 'nikeplus', 'makeitcount'], 'neutral'),
           (['disappointing', 'day', 'attended', 'car', 'boot', 'sale', 'raise', 'funds', 'sanctuary',
             'total', 'entry', 'fee', 'sigh'], 'negative'),
           (['taking', 'irish', 'car', 'bombs', 'strange', 'australian', 'women', 'drink', 'head',
             'hurts'], 'negative'),
           (['bloodwork', 'arm', 'hurts'], 'negative')]
featureList = ['hey', 'cici', 'luv', 'mixtape', 'drop', 'soon', 'fantasy', 'ride', 'heard',
'congrats', 'ncaa', 'franklin', 'wild', 'share', 'jokes', 'quotes', 'music', 'photos', 'news',
'articles', 'facebook', 'twitter', 'night', 'twitter', 'thelegionofthefallen', 'cimes', 'awfully',
'finished', 'mi', 'run', 'pace', 'gps', 'nikeplus', 'makeitcount', 'disappointing', 'day', 'attended',
'car', 'boot', 'sale', 'raise', 'funds', 'sanctuary', 'total', 'entry', 'fee', 'sigh', 'taking',
'irish', 'car', 'bombs', 'strange', 'australian', 'women', 'drink', 'head', 'hurts', 'bloodwork',
'arm', 'hurts']
for row in inpTweets:
    sentiment = row[0]
    tweet = row[1]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    tweets.append((featureVector, sentiment));
#end loop
    #start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end
    #Read the tweets one by one and process it
inpTweets = csv.reader(open('tweets.csv', 'r'), delimiter=',', quotechar='|')
stopWords = getStopWordList('stopwords.txt')
featureList = []

# Get tweet words
tweets = []
for row in inpTweets:
    sentiment = row[0]
    tweet = row[1]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#end loop
# Remove featureList duplicates
featureList = list(set(featureList))
# Extract feature vector for all tweets in one shote
training_set = nltk.classify.util.apply_features(extract_features, tweets)
# Train the classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
# Test the classifier
testTweet = 'Hey, this is twitter sentiment analysis using twitterapi'
processedTestTweet = processTweet(testTweet)
print (NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet))))
