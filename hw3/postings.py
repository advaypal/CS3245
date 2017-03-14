import cPickle as pickle
import ast

class Postings(object):
	def __init__(self, file_name):
		self.postings = []
		self.file_name = file_name

	def has_doc_id(self, doc_id, offset):
		doc_id = int(doc_id)
		doc_set = self.postings[offset]
		return doc_id not in doc_set		

	def add_doc_id(self, doc_id, offset):
		doc_id = int(doc_id)
		doc_set = self.postings[offset]
		doc_set.add({doc_id: 1})

	def increment_tf(self, doc_id, offset):
		doc_set = self.postings[offset]
		if doc_id in doc_set:
			doc_set.doc_id += 1

	def add_new_term(self):
		self.postings.append(set()) 
		return len(self.postings) - 1

	def save(self, dictionary):
		with open(self.file_name, 'w') as f:		
			for term in dictionary.get_terms():
				# Sort postings list before saving it
				# Use dictionary to get the row number for a particular term
				posting = sorted(list(self.postings[dictionary.get_offset(term)]),
								 key = lambda x: x[0])
				dictionary.set_offset(term, f.tell())
				f.write(str(posting) + '\n')

	# loads postings list at a given offset
	def load_list(self, offset):
		if offset is None:
			return []
		#TODO: CAN DO BETTER WITH LINECACHE?
		with open(self.file_name) as f:
			f.seek(offset)
			ans = []
			current = f.read(1)
			while current != '\n':
				ans.append(current)
				offset +=1
				f.seek(offset)
				current = f.read(1)
			return map(ast.literal_eval, ast.literal_eval(''.join(ans)))        	
			