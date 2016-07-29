class LinkedList():

	def __init__(self) :
		self._head = None	
		self._size = 0

	def add_node(self, e):
		newest = Node(e, self._head)
		self._head = newest
		self._size += 1

	def add_new_tail(self,e):
		newest = Node(e)
		self._tail = newest
		self._size += 1

	def remove_first(self):		
		if not self.is_empty():
			self._head = self._next
			self._size -= 1

	def is_empty(self):
		return self_size == 0

	def push(self,e):
		self._head = Node(e, self._head)
		self._size += 1	

	def top(self):
		if not self.is_empty()
			return self._head._element

	def pop(self):
		if not self.is_empty():
			answer = self._head._element
			self._head = self._head._next
			self._size -= 1

			return answer


class Node():

	__slots__ = '_element,', '_next'

	def __init__(self, e, next = None):
		self._element = e
		self._next = next


