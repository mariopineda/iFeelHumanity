import string
from collections import Counter
import datetime
import os
import sys

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
  words = tweet.split()

  # Remove stopwords
  #tmp = ' '.join([i for i in words if i not in stopwords])
  tmp = [i for i in words if i.lower() not in stopwords]

  # Remove punctuation
  tmp2 = ' '.join(tmp)
  tmp3 = tmp2.translate(None, string.punctuation)

  tweet = tmp3 
  print('OUT: %s' % tmp3)
  words_list.extend(tweet.split())

# Count word occurences
wordCounts = Counter(words_list)

file = open('/home/mpineda/iFeelHumanity/wordCounts.txt','w')
for letter, count in wordCounts.most_common(100):
  file.write('%s\t%d\n' % (letter, count))
file.close()

# Save top three words
file = open('/home/mpineda/iFeelHumanity/topThreeWords.txt','w')
for letter, count in wordCounts.most_common(3):
  file.write('%s\n' % (letter))
file.close()


# Save words to file
file = open('/home/mpineda/iFeelHumanity/wordList.txt','w')
for word in words_list:
  file.write('%s\n' % word)
file.close()

# Rename tweet file
dt = str(datetime.datetime.now())
newname = '/home/mpineda/iFeelHumanity/tweets_'+dt+'.txt'
os.rename('/home/mpineda/iFeelHumanity/morgue/tweets.txt', newname)