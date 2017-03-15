import nltk
import linecache
import sys
import os
import cPickle as pickle
from dictionary import Dictionary
from postings import Postings

def get_argument_value(flag):
	return sys.argv[sys.argv.index(flag) + 1]

def main():
	#Get arguments
	directory_of_documents = get_argument_value('-i')
	dictionary_file = get_argument_value('-d')
	postings_file = get_argument_value('-p')
	build_index(directory_of_documents, dictionary_file, postings_file)

def build_index(directory, dictionary_file, postings_file):
	files = os.listdir(directory)
	dictionary = Dictionary(dictionary_file)
	postings = Postings(postings_file)
	stemmer = nltk.stem.porter.PorterStemmer()
	last = ''
	for doc_id in files:
		dictionary.add_doc()
		line_number = 1
		# Use linecache to get line
		line = linecache.getline(os.path.join(directory, doc_id), line_number)
		while line != '':
			# tokenize lines into sentences
			sentences = nltk.sent_tokenize(line)
			for sentence in sentences:
				# tokenize sentence
				tokens = nltk.word_tokenize(sentence)
				for token in tokens:
					# apply stemming and case folding
					stemmed_token = stemmer.stem(token).lower()
					# if term already exists in dictionary, we find row number
					if dictionary.has_term(stemmed_token):
						offset = dictionary.get_offset(stemmed_token) 
						# If postings already has doc id, then increment tf,
						# Else increment df
						if postings.has_doc_id(doc_id, offset):
							postings.increment_tf(doc_id, offset)	
						else:
							dictionary.increment_df(stemmed_token)
					# else, we add it to dictionary and postings
					else:
						offset = postings.add_new_term()
						postings.add_doc_id(doc_id, offset)
						dictionary.add_new_term(stemmed_token, offset)
						
			line_number += 1
			line = linecache.getline(os.path.join(directory, doc_id), line_number)
			# Store doc length
			dictionary.add_doc_length(doc_id, postings.get_tf_list)
	# save data
	postings.save(dictionary)
	dictionary.save()

if __name__ == "__main__":
	main()
