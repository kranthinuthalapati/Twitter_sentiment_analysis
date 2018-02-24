# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 02:21:13 2018

@author: Kranthi
"""
#import the required package to transfer the output to a file
import sys
sys.stdout=open("kls.txt","w")
import twitter
# Import required package to process data in JSON format
#import jsonlib
import simplejson
try:
    import json
except ImportError:
    import simplejson as json
# Import the required methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
# Variables containing the user credentials to access Twitter API 
a_t = '966705979730534401-XIuK3UVe3lv5q0ofQD9wXEyEPKjTr3o'
a_s = '6mkCEmDUtNjmI0ApIDr5xSwYAOOahMA8yS4GwZwOz7sI7'
c_k = 'Sae0y3NbLJcyCzv6vaG7X3mrI'
c_s = 'XpLzWP7gizzEAidsl8kcPAHb4zJaLrODhPnIUQFMxtuZ3LUMbY'

oauth = OAuth(a_t, a_s, c_k, c_s)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print (json.dumps(tweet))  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
      
    if tweet_count <= 0:
        break 
sys.stdout.close()
    