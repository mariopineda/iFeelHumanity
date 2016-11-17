import string
from collections import Counter
import datetime
import os
import sys
import twitter
import random

# Check that file with tweet data exists
try:
    file = open('/home/mpineda/iFeelHumanity/tweets.txt')
    file.close()
except IOError:  # FileNotFoundError in Python 3
    print "File not found: {}".format('tweets.txt')
    sys.exit()

tweets = [line.rstrip('\n') for line in open('/home/mpineda/iFeelHumanity/tweets.txt')]
stopwords = [line.rstrip('\n') for line in open('/home/mpineda/iFeelHumanity/stopwords.txt')]
stopwords = filter(None, stopwords)

# Remove stop words from tweets
words_list = []
for tweet in tweets:
  print('IN: %s' % tweet)
  tweet = tweet.translate(None, string.punctuation) # Remove punctuation
  words = tweet.split() # Split into separate words

  # Remove stopwords
  tmp = [i for i in words if i.lower() not in stopwords]
  tweet = tmp
  print('OUT: %s' % ' '.join(tweet))
  words_list.extend(tweet)

# Get word frequencies
wordCounts = Counter(words_list)

# Save word frequences of the top 100 most common words to file
file = open('/home/mpineda/iFeelHumanity/wordCounts.txt','w')
for letter, count in wordCounts.most_common(100):
  file.write('%s\t%d\n' % (letter, count))
file.close()

#------------------------------------------------------------------------
# Random sampling of three words by frequency. 
# Note that since multiple occurences of words are represented as multiple 
# identical items in the wordPop list we need to remove the first two 
# sampled words from the list to avoid resampling of the same words 
#------------------------------------------------------------------------
wordPop = [] # A list of words, each one repeated as many time as it occurs
sampleWords = [] # List of the three sampled words
for letter, count in wordCounts.most_common(10):
  wordPop += [letter] * count
word = random.sample(wordPop, 1) # Sample 1st word
sampleWords += word 
s = ''.join(word)
while s in wordPop: wordPop.remove(s) # Remove 1st word from population to avoid resampling

word = random.sample(wordPop, 1) # Sample 2nd word
sampleWords += word 
s = ''.join(word)
while s in wordPop: wordPop.remove(s) # Remove 2st word from population to $

word = random.sample(wordPop, 1) # Sample 3rd word
sampleWords += word 

# Save top three words & move old file to morgue
#dt = str(datetime.datetime.now())
#newname = '/home/mpineda/iFeelHumanity/morgue/topThreeWords_'+dt+'.txt'
#os.rename('/home/mpineda/iFeelHumanity/topThreeWords.txt', newname)

#file = open('/home/mpineda/iFeelHumanity/topThreeWords.txt','w')
#for i in sampleWords:
#  file.write('%s\n' % i)
#file.close()

# Save words to file & move old file to morgue
#newname = '/home/mpineda/iFeelHumanity/morgue/wordList_'+dt+'.txt'
#os.rename('/home/mpineda/iFeelHumanity/wordList.txt', newname)

#file = open('/home/mpineda/iFeelHumanity/wordList.txt','w')
#for word in words_list:
#  file.write('%s\n' % word)
#file.close()

# Rename tweet file
#newname = '/home/mpineda/iFeelHumanity/morgue/tweets_'+dt+'.txt'
#os.rename('/home/mpineda/iFeelHumanity/tweets.txt', newname)

# Tweet out
#-----------------------------------------------------------------------
# post a new status
# twitter API docs: https://dev.twitter.com/docs/api/1/post/statuses/update
#-----------------------------------------------------------------------
#
# Load twitter authorization keys (these are secret are ignored by git)
#
file = open('/home/mpineda/iFeelHumanity/consumer_key.txt', 'r')
consumer_key = file.read()
consumer_key = consumer_key.rstrip('\n') # Remove trailing \n
file.close()

file = open('/home/mpineda/iFeelHumanity/consumer_secret.txt', 'r')
consumer_secret = file.read()
consumer_secret = consumer_secret.rstrip('\n')
file.close()

file = open('/home/mpineda/iFeelHumanity/access_token.txt', 'r')
access_token = file.read()
access_token = access_token.rstrip('\n')
file.close()

file = open('/home/mpineda/iFeelHumanity/access_token_secret.txt', 'r')
access_token_secret = file.read()
access_token_secret = access_token_secret.rstrip('\n')
file.close()

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

new_status = "I feel " + sampleWords[0] + ". I feel " + sampleWords[1] + ". I feel " + sampleWords[2] + ". #iFeelHumanity"
status = api.PostUpdate(new_status)
#results = twitter.statuses.update(status = new_status)
print "updated status: %s" % new_status
