
class BinarTree:

	def __init__(self,e):
		self._root = Node(e)
		pass

	def add_left(self, e):
		pass

	def add_roght(self, e):
		pass

	def replace(self, p, e):
		pass

	def delete(self, p):
		pass

	def attach(self,t1, t2):
		pass

class Node:
	
	def __ini__(self,element, parent = None, left = None, right = None):
		self._element = element
		self._left = None
		self._right = None
		self._parent = parent


