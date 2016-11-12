# Before running getTweets.py the following installations have top be done:
#
# sudo pip install python-twitter

import twitter
import urllib
import random
from collections import Counter

#
# Load twitter authorization keys (these are secret are ignored by git)
#
file = open('consumer_key.txt', 'r')
consumer_key = file.read()
consumer_key = consumer_key.rstrip('\n') # Remove trailing \n
file.close()

file = open('consumer_secret.txt', 'r')
consumer_secret = file.read()
consumer_secret = consumer_secret.rstrip('\n')
file.close()

file = open('access_token.txt', 'r')
access_token = file.read()
access_token = access_token.rstrip('\n')
file.close()

file = open('access_token_secret.txt', 'r')
access_token_secret = file.read()
access_token_secret = access_token_secret.rstrip('\n')
file.close()

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)
#print(api.VerifyCredentials())

# Documentation for twitter search api: https://dev.twitter.com/rest/reference/get/search/tweets
results = api.GetSearch(raw_query="q=%22I%20feel%22%20lang%3Aen&count=100&result_type=recent")

# Define custom black listed words (that should be removed from tweets)
black_list = ['rt', '&amp', '&amp;', 'weed', 'homo', 'gay', 'ho', 'hoes']

# Load List of Dirty Naughty Obscene and Otherwise Bad Words (that will be used to bleep-out words)
#ldnoobw = [line.rstrip('\n') for line in open('ldnoobw.txt')]
ldnoobw = urllib.urlopen("https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en").read()
ldnoobw = ldnoobw.split('\n')
ldnoobw = filter(None, ldnoobw)

tweet_list = []
word_list = []

for result in results:

    # Convert current tweet to ascii
    tmp = result.text
    tweet = tmp.encode('ascii', 'ignore')

    #    s.encode('utf-8','replace')
    if not 'http' in tweet and len(tweet) < 140:

        # Turn upper cases to lower cases
        tmp = tweet.lower()
        tweet = tmp

        # Remove blacklisted words
        words = tweet.split()
        tmp = ' '.join([i for i in words if i not in black_list])
        tweet = tmp

        # Replace LDNOOBW with <bleep>
        for bad in ldnoobw:
          tweet = tweet.replace(" "+bad,' <bleep>')

        # Remove hashtags
#        tmp = ' '.join(word for word in tweet.split(' ') if not word.startswith('#'))
#        tweet = tmp

        # Remove words that start with @
        tmp = ' '.join(word for word in tweet.split(' ') if not word.startswith('@'))
        tweet = tmp

        # Split sentence into individual words
        words = tweet.split()
        word_list.append(words)

        tweet_list.append(tweet)

        # Remove duplicate tweets
        tweet_list = list(set(tweet_list))

# Save cleaned up list of tweets to file
file = open('tweets.txt', 'w')
for tweet in tweet_list:
  file.write('%s\n' % tweet)
file.close()

print("Scraped number of tweets: ", len(results))
print("Cleaned number of tweets: ", len(tweet_list))
