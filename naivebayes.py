# Kari Green
# cngreen
# naivebayes.py
#----------------------------------------

import sys
import os
import re
import math

from processDocument import *

#----------------------------------------------------------------------------------------------------------------------------------------
def trainNaiveBayes(filenames, path):
	class_probabilities = determineClassProbs(filenames)

	word_probabilities = determineWordProbs(filenames, path)

	return class_probabilities, word_probabilities

def testNaiveBayes(filename):
	predicition = ''
	return predicition

def identifyFileType(filename):
	# identifies the categories from the filenames
	filename = re.sub(r'.txt', '', filename)
	filename = re.sub(r'[0-9]', '', filename)
	return filename

def determineClassProbs(filenames):
	# determines the class probability for each category c_j
	# prob c_j =  doc_j / total docs
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
	# Determines the number of words in a text
	count = 0

	for w in words.keys():
		count += words[w]

	return count

def calculateProb(occurrences, words, vocab_size):
	# Determines the probability of an individual word in the text of the given category
	# Use the log of the probability to prevent floating-point underflow
	probability = 0

	numerator = occurrences + 1
	denominator = words + vocab_size

	probability = float(numerator)/float(denominator)

	probability = math.log10(probability)

	return probability

def determineWordProbs(filenames, path):
	# Determines the probability of each word in the vocabulary for each category
	word_probs = {}
	text, vocab = determineVocab(filenames,path)

	vocab_size = len(vocab)

	for c in text.keys():
		word_probs[c] = {}
		number_words = determineNumberofWords(text[c])
		print (c, number_words)

		for word in vocab:
			if word in text[c].keys():
				word_probs[c][word] = calculateProb(text[c][word], number_words, vocab_size)
			else:
				word_probs[c][word] = calculateProb(0, number_words, vocab_size)

	return word_probs

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

	print(filenames)

	targetFile = open('naivebayes.output', 'w+')

	output =  ''
	targetFile.write(output)


if __name__ == "__main__": 
	main()