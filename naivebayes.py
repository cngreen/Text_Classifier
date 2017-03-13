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
def trainNaiveBayes(filenames, path):
	class_probabilities = {}
	class_probabilities = determineClassProbs(filenames)

	word_probabilities = {}
	vocab_size = 0
	return class_probabilities, word_probabilities, vocab_size

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

def determineTexts(filenames, path):
	# determines the vocabulary size and the Text_j for each Category c_j
	# text[category] = ['a' ' b' 'c']
	text = {}

	for filename in filenames:
		my_class = identifyFileType(filename)
		if my_class not in text.keys():
			text[my_class] = []

		path2file = os.path.join(path, filename)
		lines = [line.rstrip('\n') for line in open(path2file)] #get all the text lines from the file

		for line in lines:
			line.strip()
			if line != '':
				temp = []
				temp = tokenizeText(line)

			text[my_class].extend(temp)

	vocab_size = 0
	for c in text.keys():
		vocab_size += len(text[c])

	return text, vocab_size

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