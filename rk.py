# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 01:31:20 2018

@author: Kranthi
"""
import sys
sys.stdout=open("one.txt","w")
#import regex
import re
#start process_tweet
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
#end
#Read the tweets one by one and process it
fp = open('tws.txt', 'r')
line = fp.readline()
while line:
    processedTweet = processTweet(line)
    print (processedTweet)
    line = fp.readline()
#end loop
fp.close()
sys.stdout.close()

