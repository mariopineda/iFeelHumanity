# sudo pip install -U nltk

import twitter
import random
from collections import Counter
from nltk.corpus import stopwords

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

file = open('access_token_key.txt', 'r')
access_token_key = file.read()
access_token_key = access_token_key.rstrip('\n')
file.close()

file = open('access_token_secret.txt', 'r')
access_token_secret = file.read()
access_token_secret = access_token_secret.rstrip('\n')
file.close()

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)
#print(api.VerifyCredentials())
results = api.GetSearch(raw_query="q=%22I%20feel%22%20lang%3Aen&count=10")

black_list = ['rt']

tweet_list = []
word_list = []

file = open('tweets.txt', 'w')
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

        # Remove hashtags
        tmp = ' '.join(word for word in tweet.split(' ') if not word.startswith('#'))
        tweet = tmp

        # Remove words that start with @
        tmp = ' '.join(word for word in tweet.split(' ') if not word.startswith('@'))
        tweet = tmp

        file.write('%s\n' % tweet)

        # Split sentence into individual words
        words = tweet.split()
        word_list.append(words)

        tweet_list.append(tweet)

file.close()
