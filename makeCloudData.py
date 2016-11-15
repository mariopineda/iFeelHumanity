import string
from collections import Counter
import datetime
import os
import sys
import twitter

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

# Save top three words & move old file to morgue
dt = str(datetime.datetime.now())
newname = '/home/mpineda/iFeelHumanity/morgue/topThreeWords_'+dt+'.txt'
os.rename('/home/mpineda/iFeelHumanity/topThreeWords.txt', newname)

file = open('/home/mpineda/iFeelHumanity/topThreeWords.txt','w')
for letter, count in wordCounts.most_common(3):
  file.write('%s\n' % (letter))
file.close()

# Save words to file & move old file to morgue
newname = '/home/mpineda/iFeelHumanity/morgue/wordList_'+dt+'.txt'
os.rename('/home/mpineda/iFeelHumanity/wordList.txt', newname)

file = open('/home/mpineda/iFeelHumanity/wordList.txt','w')
for word in words_list:
  file.write('%s\n' % word)
file.close()

# Rename tweet file
dt = str(datetime.datetime.now())
newname = '/home/mpineda/iFeelHumanity/morgue/tweets_'+dt+'.txt'
os.rename('/home/mpineda/iFeelHumanity/tweets.txt', newname)

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
#print(api.VerifyCredentials())


words = [line.strip('\n') for line in open('/home/mpineda/iFeelHumanity/topThreeWords.txt')]
new_status = "I feel " + words[0] + ". I feel " + words[1] + ". I feel " + words[2] + ". #iFeelHumanity"
status = api.PostUpdate(new_status)

results = twitter.statuses.update(status = new_status)
print "updated status: %s" % new_status
