### Brett Atkinson
### September, 2015
### Software Design - Project 1.1
### Expanded script specifically for collecting data during events


def poli_twitter_analysis():
	"""This function parses Twitter to determine the average sentiment towards political figures during an event"""

	# Fixed the spacing in your list -- consistency is always a good thing
	candidates = ['trump', 'walker', 'fiorina', 'carson', 'cruz', 'rubio', 'huckabee', 'paul', 'kasich', 'christie', 'bush', 'clinton', 'sanders', "o'malley"] #list of searches to use

	twtNum = 50 #number of tweets to search for each time

	t = Twitter()
	i = None
	twtstext = []
	twtsdate = []
	twtsauthor = []
	twtscandi = []
	twtssenti = []

	for item in candidates:
		for j in range(1): # j is never being used -- this is extraneous
			# again, a little strange that you're setting start=None
			for tweet in t.search(item, start=i, count=twtNum):
				# especially since the variable names aren't 100% clear and this looks
				# like the bulk of this function, a little more documentation might be nice
				twtscandi.append(item)
				twtstext.append(tweet.text)
				m = tweet.text
				twtsdate.append(tweet.date)
				twtsauthor.append(tweet.author)
				[senti,objec] = sentiment(m)
				twtssenti.append(senti)

	zipped1 = zip(twtscandi, twtssenti)
	zipped2 = zip(twtscandi, twtsdate, twtsauthor, twtstext, twtssenti)

	timestr = time.strftime("%Y%m%d%H%M%S")

	filename = timestr + '.txt'
	f = open(filename, 'w')
	f.write(' '.join(map(str, zipped1)))
	f.close()

	filename = 'tweets_' + timestr + '.txt'
	f = open(filename, 'w')
	f.write(' '.join(map(str, zipped2)))
	f.close()

	print 'Complete'

# again, imports at the top
from pattern.en import sentiment #import required packages
from pattern.web import Twitter
import time
import csv

# why is it running twice? Leave a comment so people who read your code know!
for i in range(2):
	print 'Running...'
	poli_twitter_analysis() #run function
	time.sleep(10)

# Once again, smaller functions and a uniting function to chain them together would be easier to read/maintain

# It's awesome that you plotted your results in matlab -- in the future, matplotlib's interface is almost identical,
# you'd probably pick it up pretty quickly
