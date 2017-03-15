from dictionary import Dictionary
from postings import Postings
import nltk
import math
from heapq import nlargest

class Searcher(object):
	def __init__(self, dictionary_file, postings_file):
		self.dictionary = Dictionary(dictionary_file)
		self.postings = Postings(postings_file)
		self.dictionary.load()
		self.rank_limit = 10

	#evaluates a query
	def evaluate_query(self, query):
		N = self.dictionary.get_do c_count
		scores = {}
		tokens = nltk.word_tokenize(query)
		query_map = {}

		# Build frequency table for query
		for token in tokens:
			term = stemmer.stem(token).lower()
			if term in query_map:
				query_map[term] += 1
			else:
				query_map[term] = 1

		for token in tokens:
			term = stemmer.stem(token).lower()
			df = self.dictionary.get_df(term)
			w_tq = (1 + math.log(query_map[term], 10)) * math.log(N / df, 10)
			query_map[term] = w_tq

			offset = self.dictionary.get_offset(term)
			postings = self.postings.load_list(offset)

			for posting in postings:
				doc = posting[0]
				w_td = 1 + math.log(posting[1], 10)
				scores[doc] += w_td * w_tq

		query_length = math.sqrt(sum(map(lambda x: x * x , query_map.values())))
		heap = []
		for doc, value in scores.iteritems():
			doc_length = self.dictionary.get_doc_length(doc)
			scores[doc] = value / (query_length * doc_length)
		
		#get top K from heap
		return map(lambda x: x[0], nlargest(self.rank_limit, scores.items(), 
									key = lambda x: x[1]))

				



			
			