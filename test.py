# Kari Green
# cngreen
# naivebayes.py
#----------------------------------------

import sys
import os
import re
import operator

from processDocument import *

#----------------------------------------------------------------------------------------------------------------------------------------

def identifyFileType(filename):
	filename = re.sub(r'.txt', '', filename)
	filename = re.sub(r'[0-9]', '', filename)
	return filename

def determineClassProbs(filenames):
	class_probabilities = {}
	file_count = 0
	for filename in filenames:
		file_count += 1
		file_type = identifyFileType(filename) 
		if file_type not in class_probabilities.keys():
			class_probabilities[file_type] = 1
		else:
			class_probabilities[file_type] += 1

	for my_class in class_probabilities.keys():
		class_probabilities[my_class] = float(class_probabilities[my_class])/float(file_count)

	return class_probabilities

def determineVocab(filenames, path):
	# determines the vocabulary ['a' 'b' 'c']
	# and the Text_j for each Category c_j
	# text[category] = ['a': 1 ' b': 3 'c': 4] (number of occurrences of a term)
	text = {}
	vocab = []

	for filename in filenames:
		my_class = identifyFileType(filename)
		if my_class not in text.keys():
			text[my_class] = {}

		path2file = os.path.join(path, filename)
		lines = [line.rstrip('\n') for line in open(path2file)] #get all the text lines from the file

		for line in lines:
			line.strip()
			if line != '':
				temp = []
				temp = tokenizeText(line)

			for t in temp:
				if t not in vocab:
					vocab.append(t)

				if t not in text[my_class].keys():
					text[my_class][t] = 1
				else:
					text[my_class][t] += 1

	return text, vocab

def determineNumberofWords(words):
	count = 0

	for w in words.keys():
		count += words[w]

	return count

def calculateProb(occurrences, words, vocab_size):
	probability = 0

	numerator = occurrences + 1
	denominator = words + vocab_size

	probability = float(numerator)/float(denominator)

	return probability

def determineWordProbs(filenames, path):
	word_probs = {}
	text, vocab = determineVocab(filenames,path)

	vocab_size = len(vocab)

	for c in text.keys():
		word_probs[c] = {}
		number_words = determineNumberofWords(text[c])
		print (c, number_words)

		for word in vocab:
			if word in text[c].keys():
				print calculateProb(text[c][word], number_words, vocab_size)
			else:
				print calculateProb(0, number_words, vocab_size)


def identifyAcronymsAbbrev2(input):
	#finds formatted numbers
	tokens = []
	if '.' not in input:
		return input, tokens

	match = re.findall(r'\w+[.]+\w+[.\w*]*', input)
	if match != None:
		for m in match:
			m = m.strip()
			tokens.append(m)
		input = re.sub(r'\w+[.]+\w+[.\w*]*', '', input)

	return input, tokens
	
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
def main():
	filenames = []
	#print 'Argument List:', str(sys.argv)
	try: 
		foldername = str(sys.argv[1])
	except:
		sys.exit("ERROR: no folder of that name")

	path = os.path.join(os.getcwd(), foldername) #specified folder

	for filename in os.listdir(path): #for all files in specified folder
		filenames.append(filename)

		path2file = os.path.join(path, filename)
		lines = [line.rstrip('\n') for line in open(path2file)] #get all the text lines from the file

		#for each line in the file
		#for line in lines:
			#print line




	determineWordProbs(filenames, path)



	targetFile = open('naivebayes.output', 'w+')

	output =  ''
	targetFile.write(output)


if __name__ == "__main__": 
	main()