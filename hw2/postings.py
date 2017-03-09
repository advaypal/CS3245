import cPickle as pickle
import ast

class Postings(object):
	def __init__(self, file_name):
		self.postings = []
		self.all_docs = []
		self.file_name = file_name
	
	def add_doc(self, doc_id):
		doc_id = int(doc_id)
		self.all_docs.append(doc_id)

	def add_doc_id(self, doc_id, offset):
		doc_id = int(doc_id)
		doc_set = self.postings[offset]
		if doc_id not in doc_set:
			doc_set.add(doc_id)
			return True
		else:
			return False

	def add_new_term(self):
		self.postings.append(set()) 
		return len(self.postings) - 1

	def save(self, dictionary):
		with open(self.file_name, 'w') as f:		
			f.write(str(sorted(self.all_docs)) + '\n')
			for term in dictionary.get_terms():
				#sort postings list before saving it
				#Use dictionary to get the row number for a particular term
				posting = sorted(list(self.postings[dictionary.get_offset(term)]))
				dictionary.set_offset(term, f.tell())
				f.write(str(posting) + '\n')

	#loads postings list at a given offset
	def load_list(self, offset):
		if offset is None:
			return []
		with open(self.file_name) as f:
			f.seek(offset)
			ans = []
			current = f.read(1)
			while current != '\n':
				ans.append(current)
				offset +=1
				f.seek(offset)
				current = f.read(1)
			return map(int, ast.literal_eval(''.join(ans)))        	


