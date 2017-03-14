from dictionary import Dictionary
from postings import Postings
from utils import *

class Searcher(object):
	def __init__(self, dictionary_file, postings_file):
		self.dictionary = Dictionary(dictionary_file)
		self.postings = Postings(postings_file)
		self.dictionary.load()
		self.all_docs = self.postings.load_list(0)

	#evaluates a query assuming it is in RPN 
	def evaluate_query(self, parsed_query):
		stack = []
		while(len(parsed_query) != 0):
			element = parsed_query.pop(0)
			if element == 'NOT':
				operand = stack.pop()
				stack.append(self.evaluate_NOT(operand))
			elif element == 'AND':
				first_operand = stack.pop()
				second_operand = stack.pop()
				stack.append(self.evaluate_AND(first_operand, second_operand))
			elif element == 'OR':
				first_operand = stack.pop()
				second_operand = stack.pop()
				stack.append(self.evaluate_OR(first_operand, second_operand))
			else:
				stack.append(element)
		value = stack.pop()
		if not isinstance(value, list):
			offset = self.dictionary.get_offset(value)
			value = self.postings.load_list(offset)
		return value

	def evaluate_AND(self, first, second):
		if not isinstance(first, list):
			offset = self.dictionary.get_offset(first)
			first = self.postings.load_list(offset)
		if not isinstance(second, list):
			offset = self.dictionary.get_offset(second)
			second = self.postings.load_list(offset)
		return skip_intersection(first, second)
			
	def evaluate_OR(self, first, second):
		if not isinstance(first, list):
			offset = self.dictionary.get_offset(first)
			first = self.postings.load_list(offset)
		if not isinstance(second, list):
			offset = self.dictionary.get_offset(second)
			second = self.postings.load_list(offset)
		return union(first, second)

	def evaluate_NOT(self, operand):
		if not isinstance(operand, list):
			offset = self.dictionary.get_offset(operand)
			operand = self.postings.load_list(offset)
		return difference(self.all_docs, operand)








