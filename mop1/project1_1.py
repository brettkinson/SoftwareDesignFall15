### Brett Atkinson
### September, 2015
### Software Design - Project 1


def poli_twitter_analysis():
	"""This function parses Twitter to determine the average sentiment towards a user-defined political figure"""

	print 'This program measures the average sentiment of the populous towards a political candidate through the analysis of recent tweets' #introduce program to user
	# Lots of ways to print a blank line -- you could also have used \n
  print
	print 'Enter the name of a candidate:'
	x = raw_input('> ') #receives name of candidate to search for
	print 'Enter number of tweets to search (max = 100)'
	twtNumstr = raw_input('> ') #recieve number of tweets to search for
	twtNum = int(twtNumstr) #convert to int to use in search


	if twtNum <= 1: #check if an invalid number was entered, and if so, correct it to either the minimum or maximum allowed
    # Great that you're handling the error case!
		twtNum = 2
		print 'Invalid number entered. The minimum of 2 tweets will be used.'
	elif twtNum > 100:
		twtNum = 100
		print 'Invalid number entered. The maximum of 100 tweets will be used.'

	t = Twitter() #search for tweets containing user-defined key word
	i = None
	twts = []
	for j in range(1):
    # It's a little strange that you're setting start=None -- is this extraneous?
		for tweet in t.search(x, start=i, count=twtNum):
			twts.append(tweet.text)


	senti_count = 0 #predefine sentiment variable
	for entry in twts: #loop through all tweets found
		[senti,objec] = sentiment(entry) #sentiment analysis of tweets
		senti_count = senti_count + senti

	res = senti_count/twtNum #get average sentiment of all tweets parsed

	print 'Result:'

  # Any time you see something really repetitive like this in your code, it's
  # might be a good idea to write a function you can reuse
	if res >= -0.01 and res <= 0.01:
		print 'Overwhelmingly neutral!'
	elif res > 0.01 and res <= 0.1:
		print 'Somewhat positive'
		print("%s out of 1.0" % res)
	elif res > 0.1 and res <= 0.5:
		print 'Pretty positive'
		print("%s out of 1.0" % res)
	elif res > 0.5:
		print 'Very positive!'
		print("%s out of 1.0" % res)
	elif res < -0.01 and res >= -0.1:
		print 'Somewhat negative'
		print("%s out of -1.0" % res)
	elif res < -0.1 and res >= -0.5:
		print 'Pretty negative'
		print("%s out of -1.0" % res)
	elif res < 0.5:
		print 'Very negative...'
		print("%s out of -1.0" % res)

	twtTrends = t.trends(cached=False) #import current twitter trends (worldwide)
	twtTrendsLower = [runthrough.lower() for runthrough in twtTrends]
	xLower = x.lower()
	if any(xLower in s for s in twtTrendsLower): #check to see if the user's search matches any of the current trends
		print 'Your search is trending!'
		matching = [s for s in twtTrendsLower if xLower in s]
		for entry in matching:
			if entry[0] == '#':
				print entry
			else:
				print '#' + entry

	print 'Do you want to read the tweets? (y/n)' #user can read the tweets used
	yay_or_nay = raw_input('> ')
	if yay_or_nay == 'y': #only complete if user requests
		for entry in twts: #loop through all tweets found
			print entry #print each tweet with a blank line separating each
			print

# It's generally good practice to import at the top of your file -- that way, there's a standard place to look to see
# what a particular module's dependencies are
from pattern.en import sentiment #import required packages
from pattern.web import Twitter

poli_twitter_analysis() #run function

# This is a lot to be doing in a single function -- it might be easier to read/maintain your code if you broke the problem down
# into a list of smaller tasks and wrote a function to accomplish each, then used a "master function" to chain them all together

# Also, naming your files meaningfully is as important as naming your variables meaningfully -- "project1_1.py" is fine in this context,
# but keep that in mind as your projects get bigger
