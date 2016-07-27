class LinkedQueue():

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size


	def is_empty(self):
		return self._size == 0

	def first(self):
		return self._head._element

	def last(self):
		return self._tail._element

	def dequeue(self):		
		if not self.is_empty():
			answer = self._head._element
			self._head = self._head._next
			self._size -= 1

			return answer

	def enqueue(self, e):
		node = Node(e)
		if self.is_empty():
			self._head = node
		else:
			self._tail._next = node

		self._tail = node
		self._size += 1


class CircularLinkedQueue():

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size


	def is_empty(self):
		return self._size == 0

	def first(self):
		return self._tail._next._element

	def last(self):
		return self._tail._element

	def dequeue(self):	
		old_head = self._tail._next._element	
		if self._size == 1:
			self._tail._next = None
		else:
			self._tail._next = old_head._next

		self._size -= 1
		return old_head._element

	def enqueue(self, e):
		node = Node(e)
		if self.is_empty():
			newest._next = newest
		else:
			newest._next = self._tail._next		
		
		self._tail = node
		self._size += 1

	def rotate(self):

		if self._size > 1:
			self._tail = self._tail._next

class Node():

	__slots__ = '_element,', '_next'

	def __init__(self, e, next = None):
		self._element = e
		self._next = next