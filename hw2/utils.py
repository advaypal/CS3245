import math
import nltk

#parses query using dijkstra's shunting yard algorithm
def parse_query(query):
	stemmer = nltk.stem.porter.PorterStemmer()
	tokens = nltk.word_tokenize(query)
	output = []
	stack = []
	for token in tokens:
		if token == 'NOT':
			stack.append(token)
		elif token == 'AND':
			while (len(stack) != 0 and stack[-1] == 'NOT'):
				output.append(stack.pop())
			stack.append(token)
		elif token == 'OR':
			while (len(stack) != 0 and (stack[-1] == 'NOT' or stack[-1] == 'AND')):
				output.append(stack.pop())
			stack.append(token)
		elif token == '(':
			stack.append(token)
		elif token == ')':
			while (len(stack) != 0 and stack[-1] != '('):
				output.append(stack.pop())
			stack.pop()
		else:
			output.append(stemmer.stem(token).lower())
	
	while len(stack) != 0:
		output.append(stack.pop())
	
	return output

#returns union of 2 lists
def union(xs, ys):
	if not xs:
		return ys
	if not ys:
		return xs
	union = []
	x_index = 0
	y_index = 0
	while x_index < len(xs) and y_index < len(ys):
		x = xs[x_index]
		y = ys[y_index]
		if x == y:
			union.append(x)
			x_index += 1
			y_index += 1
		elif x < y:
			union.append(x)
			x_index += 1
		else:
			union.append(y)
			y_index += 1

	if x_index < len(xs):
		union += xs[x_index:]

	if y_index < len(ys):
		union += ys[y_index:]
	return union

#returns list difference xs - ys
def difference(xs, ys):
	if not ys:
		return xs
	if not xs:
		return []
	x_index = 0
	y_index = 0
	difference = []
	while x_index < len(xs) and y_index < len(ys):
		x = xs[x_index]
		y = ys[y_index]
		if x == y:
			x_index += 1
			y_index += 1
		else:
			difference.append(x)
			x_index += 1
	difference += xs[x_index:]
	
	return difference

#returns list intersection. Skips over 
def skip_intersection(xs, ys):
	if (not xs) or (not ys):
		return []
	x_skip_length = int(math.sqrt(len(xs)))
	y_skip_length = int(math.sqrt(len(ys)))
	intersection = []
	x_index = 0
	y_index = 0
	while x_index < len(xs) and y_index < len(ys):
		x = xs[x_index]
		y = ys[y_index] 
		if x == y:
			intersection.append(x)
			x_index += 1
			y_index += 1
		elif x < y:
			skipped_index =  x_index + x_skip_length
			if skipped_index < len(xs) and xs[skipped_index] <= y:
				x_index = skipped_index
			else:
				x_index += 1
		else:
			skipped_index =  y_index + y_skip_length
			if skipped_index < len(ys) and ys[skipped_index] <= x:
				y_index = skipped_index
			else:
				y_index += 1

	return intersection




