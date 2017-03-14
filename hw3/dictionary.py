import cPickle as pickle

class Dictionary(object):
	def __init__(self, file_name):
		self.terms = {}
		self.file_name = file_name
		self.doc_count = 0

	def add_document(self):
		self.doc_count += 1

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
			return None

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
			pickle.dump(self.terms, f)
	
	def load(self):
		with open(self.file_name) as f:
			self.terms = pickle.load(f)
	
	def get_terms(self):
		return self.terms
