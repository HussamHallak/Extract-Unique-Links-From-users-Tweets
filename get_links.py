#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import requests
import urllib2
from urlparse import urlparse
#http://www.tweepy.org/
import tweepy

config = {}
execfile("config.py", config)

#method to get a user's last  200 tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
	auth.set_access_token(config["access_key"], config["access_secret"])
	api = tweepy.API(auth)

	#set count to however many tweets you want; twitter only allows 200 at once
	number_of_tweets = 200

	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)
	
	final_urls = []
	for tweet in tweets:
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text)
		for url in urls:
			try:
				res = urllib2.urlopen(url)
				actual_url = res.geturl()
				parsed_uri = urlparse(actual_url)
				domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
				if (domain != 'https://twitter.com/' and domain != 'https://t.co/'):
					final_urls.append(actual_url)
			except:
				print "Disgarded url: The url is not external: " + url
	fh = open ("links.txt", "a")
	final_urls = list(set(final_urls))
	for link in final_urls:
		fh.write(link)
		fh.write("\n")

	fh.close()

#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line

    if len(sys.argv) >= 2:
	i = 1
	for user in sys.argv:
        	if (i < len(sys.argv)):
			get_tweets(sys.argv[i])
		i = i + 1
    else:
        print "Error: enter twitter username(s)"

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
# 	get_tweets(user)
