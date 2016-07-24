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

class LinkedStack():

	def __init__(self) :
		self._head = None	
		self._size = 0

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

class LinkedQueue():

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size


	def is_empty(self):
		return self._size == 0

	def firs(self):
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
		




class Node():

	__slots__ = '_element,', '_next'

	def __init__(self, e, next = None):
		self._element = e
		self._next = next


