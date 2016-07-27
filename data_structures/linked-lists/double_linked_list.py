class DoubleLinkedList():
	def __init__(self) :
		self._head = Node(None,None,None)	
		self._trailer = Node(None,None,None)
		self._head._next = self._trailer
		self._trailer._prev = self._head
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def _inster_between(self,e, predecessor,sucessor):
		newest = Node(e,predecessor,sucessor)
		predecessor._next = e
		sucessor._next = e
		self._size += 1

		return newest

	def _delete_node(self,node):
		predecessor = node._prev
		sucessor = node._next
		predecessor._next = node._next
		sucessor._prev = node._prev
		self._size -= 1
		node._prev = node._next = node._element = None
		return node



	def pop(self):
		pass

class Node():

	__slots__ = '_element,','_prev', '_next'

	def __init__(self, _element, _prev = None,  _next = None):
		self._element = _element
		self._next = _next
		self._prev = _prev
