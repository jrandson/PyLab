class LinkedList():

	def __init__(self) :
		self._head = None
		self._tail = None	

		self._size = 0

	def add_node(self, e):
		newest = Node(e, self._head)
		
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			newest._next = self._head
			self._head = newest


		self._size += 1

	def add_new_tail(self,e):
		newest = Node(e)
		self._tail._next = newest
		self._tail = newest
		self._size += 1

	def remove_first(self):		
		if not self.is_empty():
			self._head = self._next
			self._size -= 1

	def is_empty(self):
		return self._size == 0

	def top(self):
		if not self.is_empty():
			return self._head._element

	def pop(self):
		if not self.is_empty():
			answer = self._head._element
			self._head = self._head._next
			self._size -= 1

			return answer

	def remove_node(self,e):
		node = self._head
		if node._element == e:
			self._head = self._head._next
		else:
			while not node._next == None:
				if node._next._element == e:
					node._next = node._next._next
					break
				node = node._next

	def show_elements(self):

		if self.is_empty():
			return ''
		
		node = self._head
		elements = str(node._element) + '->' 
		
		while not node._next == None:
			node = node._next
			elements += str(node._element) + '->' 

		return elements

	def remove_repeated_without_buffer(self):
		elements = []
		node = self._head
		elements.append(node._element)
		while not node._next == None:
			node = node._next
			if node._element in elements:
				self.remove_node(node._element)
			else:
				elements.append(node._element)

	def remove_repeated_with_buffer(self):
		node = self._head
		while not node._next == None:
			node_aux = node._next
			while True:
				if node_aux._element == node._element:
					self.remove_node(node._element)

				if not node_aux._next == None:
					node_aux = node_aux._next
				else:
					break

			node = node._next

	def find_last_n(self,n):
		node = self._head
		i = 1
		elements = []
		while not node == None:			
			elements.append(node._element)		
			node = node._next

		return elements[n-1:]

	'''Add elements in descendent ord from head '''
	def add_sort(self,e):

		if self.is_empty():
			self.add_node(e)			
			return self.show_elements()
		elif e > self._head._element:			
			newest = Node(e)
			newest._next = self._head			
			self._head = newest

			return self.show_elements()
		else:
			node = self._head._next
			prev = self._head
			while node != None:
				if e >= node._element:
					newest = Node(e)
					newest._next = node
					prev._next = newest					
					return self.show_elements()

				prev = node
				node = node._next

		newest = Node(e)
		self._tail._next = newest
		self._element = newest

		return self.show_elements()

	'''Add elements in ascedent ord from head '''
	def add_sort2(self,e):

		if self.is_empty():
			self.add_node(e)			
			return self.show_elements()
		elif e < self._head._element:			
			newest = Node(e)
			newest._next = self._head			
			self._head = newest

			return self.show_elements()
		else:
			node = self._head._next
			prev = self._head
			while node != None:
				if e <= node._element:
					newest = Node(e)
					newest._next = node
					prev._next = newest					
					return self.show_elements()

				prev = node
				node = node._next

		newest = Node(e)
		self._tail._next = newest
		self._element = newest

		return self.show_elements()


			

		

class Node():
	__slots__ = '_element,', '_next'

	def __init__(self, e, next = None):
		self._element = e
		self._next = next


