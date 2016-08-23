class Tree:

	def __init__(self, p):
		self._root = p

	''' Return the position of the root of tree T,
		or None if T is empty.'''
	def root(self):
		return self._root

	'''Return True if position p is the root of Tree T'''
	def is_root(self,p):
		return self.root() == p

	'''Return the position of the parent of position p,
		or None if p is the root of T'''
	def parent(self, p):
		raise NotImplementedError('Must be implemented by sub class')

	'''Return the number of children of position p.'''
	def num_children(self,p):
		raise NotImplementedError('Must be implemented by sub class')

	'''Generate an iteration of the children of position p'''
	def children(self, p):
		raise NotImplementedError('Must be implemented by sub class')

	''' Return True if position p does not have any children.'''
	def is_leaf(self, p):
		raise NotImplementedError('Must be implemented by sub class')

	'''Return the number of positions (and hence elements) that
		are contained in tree T.'''
	def len(self, T):
		raise NotImplementedError('Must be implemented by sub class')

	'''Return True if tree T does not contain any positions.'''
	def is_empty(self):
		raise NotImplementedError('Must be implemented by sub class')

	'''Generate an iteration of all positions of tree T.'''
	def positions(self):
		raise NotImplementedError('Must be implemented by sub class')

	'''Generate an iteration of all elements stored within tree T.'''
	def iter(self, T):
		raise NotImplementedError('Must be implemented by sub class')

	def depth(self, p):
		if self.is_root(p):
			return 0
		else:
			return self(self.parent(p)) + 1


class Position:

	
	def __init__(self, e):

		self._element = e
		self._value = e*10

	def element(self):
		return self._value


p = Position(5)

p._element = 18
print p._element
print p._value