import nltk
import os
from searcher import Searcher
from utils import *
import sys

def get_argument_value(flag):
	return sys.argv[sys.argv.index(flag) + 1]

def main():
	#Get arguments
	query_file = get_argument_value('-q')
	dictionary_file = get_argument_value('-d')
	postings_file = get_argument_value('-p')
	output_file = get_argument_value('-o')
	#create searcher object
	searcher = Searcher(dictionary_file, postings_file)
	input_file = file(query_file, 'r')
	queries = input_file.read().splitlines()
	output = file(output_file, 'w')
	for query in queries:
		#no null queries
		if not query:
			continue
		parsed_query = parse_query(query)
		result = searcher.evaluate_query(parsed_query)
		doc_string = ' '.join(map(str, result))
		output.write(doc_string + '\n')
		#output.write(query + " " + doc_string + '\n')
		#output.write(query + " " + str(len(result)) + '\n')
	input_file.close()
	output.close()


if __name__ == "__main__":
	main()
