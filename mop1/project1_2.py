### Brett Atkinson
### September, 2015
### Software Design - Project 1.1
### Expanded script specifically for collecting data during events


def poli_twitter_analysis():
	"""This function parses Twitter to determine the average sentiment towards political figures during an event"""
	
	candidates = ['trump','walker', 'fiorina', 'carson', 'cruz', 'rubio', 'huckabee', 'paul', 'kasich','christie', 'bush','clinton','sanders',"o'malley"] #list of searches to use

	twtNum = 50 #number of tweets to search for each time
	
	t = Twitter() 
	i = None
	twtstext = []
	twtsdate = []
	twtsauthor = []
	twtscandi = []
	twtssenti = []

	for item in candidates:
		for j in range(1):
			for tweet in t.search(item, start=i, count=twtNum):
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
	
from pattern.en import sentiment #import required packages
from pattern.web import Twitter
import time
import csv

for i in range(2):
	print 'Running...'
	poli_twitter_analysis() #run function
	time.sleep(10)