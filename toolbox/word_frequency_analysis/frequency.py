#### Brett Atkinson
#### Software Design - FA'15
#### Project Toolbox - Word Frequency Analysis

""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """


import string
import collections

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


	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	while lines[curr_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[:curr_line-1]


	lines_low = [item.lower() for item in lines]
	lines_low = [x.replace("\r\n","") for x in lines_low]

	i=0
	for i in range(0,len(lines_low)):
		lines_low[i] = lines_low[i].split()
	i=0
	j=0
	punc = string.punctuation
	for j in range(0,len(lines_low)):
		for i in range(0,len(punc)):
			lines_low[j].replace(punc[i],'')

	#i=0
	#j=0
	#whitespc = string.whitespace
	#for j in range(0,len(lines_low)):
	#	for i in range(0,len(whitespc)):
	#		lines_low[j].replace(whitespc[i],'')
	

	print lines_low




def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	pass

if __name__ == '__main__':
	n = 10 # number of words to search for
	file_name = 'great_expectations_full_text.txt' # file name of book to use
	#get_top_n_words(get_word_list(file_name),n)
	get_word_list(file_name)