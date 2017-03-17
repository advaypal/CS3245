import cPickle as pickle
import math

class Dictionary(object):
	def __init__(self, file_name):
		self.terms = {}
		self.file_name = file_name
		self.doc_lengths = {}
		self.doc_count = 0

	def get_doc_count(self):
		return self.doc_count

	def add_doc_length(self, doc_id, tf_list):
		doc_id = int(doc_id)
		self.doc_count += 1
		self.doc_lengths[doc_id] = math.sqrt(sum(map(lambda x: pow(1 + math.log(x, 10), 2), 
													 tf_list)))

	def get_doc_length(self, doc_id):
		doc_id = int(doc_id)
		return self.doc_lengths[doc_id]

	def add_new_term(self, term, offset):
		# dict[term][0] is the df of term
		# dict[term][1] is the byte offset of the first document of the term
		# in the postings file. During indexing however, it is first the row
		# number in the postings. It is converted to offsets while the postings file is
		# saved
		pair = [1, offset]
		self.terms[term] = pair

	def get_df(self, term):
		if self.has_term(term):
			return self.terms[term][0]
		else:
			return 0

	def get_offset(self, term):
		if self.has_term(term):
			return self.terms[term][1]
		else:
			return None

	def increment_df(self, term):
		if self.has_term(term):
			self.terms[term][0] += 1

	def set_offset(self, term, offset):
		if self.has_term(term):
			self.terms[term][1] = offset

	def has_term(self, term):
		return term in self.terms

	def save(self):
		with open(self.file_name, 'w') as f:
			pickle.dump({
				'terms': self.terms,
				'doc_lengths': self.doc_lengths,
				'doc_count': self.doc_count
			}, f)
	
	def load(self):
		data = {}
		with open(self.file_name) as f:
			data = pickle.load(f)
		self.terms = data['terms']
		self.doc_lengths = data['doc_lengths']
		self.doc_count = data['doc_count']
	
	def get_terms(self):
		return self.terms
