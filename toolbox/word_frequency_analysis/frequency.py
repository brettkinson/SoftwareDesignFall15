#### Brett Atkinson
#### Software Design - FA'15
#### Project Toolbox - Word Frequency Analysis

""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """


import string
from collections import Counter
import operator

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""

	f = open(file_name,'r')

	lines = f.readlines()
	curr_line = 0

	f.close()

	lines_low = []
	lines_low_punc = []
	words_list = []


	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	while lines[curr_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[:curr_line-1]


	lines_low = [item.lower() for item in lines]
	lines_low = [x.replace("\r\n","") for x in lines_low]

	for item in lines_low:
		words_list.extend(item.split())

	chars = ['.',',','-','_','?','!','\'','\"','--']
	for item in chars:
		words_sem_punc = [x.replace(item,'') for x in words_list]

	return words_sem_punc

	

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""

	x = word_list
	freq = {}
	for item in word_list:
		if item not in freq:
			freq[item] = 0 
		freq[item] += 1

	freq_sorted = sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True)

   	print freq_sorted[0:n]


if __name__ == '__main__':
	n = 100 # number of words to search for
	file_name = 'great_expectations_full_text.txt' # file name of book to use
	print get_top_n_words(get_word_list(file_name),n)
	#get_word_list(file_name)