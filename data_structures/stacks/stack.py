class Stack:

	def __init__(self,contents = []):
		self._contents = contents
		self._min = None
		self._max = 10

	def get_contents(self):
		return self._contents
	
	def push(self, p):		
		self._contents.append(p)

		if self._min == None:
			self._min = p
		else:
			if self._min > p:
				self._min = p

	def pop(self):
		if self.len() > 0:
			return self._contents.pop()
		else:
			raise Empty("Stack is empty")

	def top(self):
		if not self.len() == 0:
			return self._contents[-1]
		else:
			raise Empty("Stack is empty")

	def is_empty(self):
		return self.len() == 0

	def len(self):
		return len(self._contents)

class SetOfstack:

	def __init__(self):
		self._stacks = []
		self._size = 0
		self._max_size = 10
		self._contents = []

	def push(self,p):
		self._contents.append(p)
		
		if len(self._contents) == self._max_size:
			self._stacks.append(self._contents)
			self._contents = []

		self._size = len(self._contents) + len(self._stacks) * self._max_size

	def pushA(self,p,i):	

		if len(self._contents) == self._max_size:
			self._stacks.append(self._contents)
			self._contents = []

	def pop(self):
		if not self.is_empty():
			if len(self._contents) == 0:
				self._contents = self._stacks[-1]
			
			self._size = len(self._size) + len(self._stacks) * self._max_size
			pop_value = self._contents.pop()

			if len(self._contents) == 0:
				self._contents = self._stacks.pop()

			return pop_value

	def popA(self,i):
		if not len(self._stacks[i]) == 0:
			pop_value = self._stacks[i].pop()
			self._size = len(self._size) + len(self._stacks) * self._max_size
			return pop_value
		else:
			return None

	def top(self):		
		if not self.is_empty():
			return self._contents[-1]

	def is_empty(self,):
		return self._size == 0

	def len(self):
		return self._size

'''
This a queuer built with stacks
'''
class MyQueue:

	def __init__(self, contents = []):	
		stack = Stack(contents)	
		self._contents = stack
		self._size = 0

	def get_content(self):
		return self._contents.get_contents()

	def reverse_stack(self):
		stack_aux = Stack()
		while  not self._contents.is_empty():
			stack_aux.push(self._contents.pop())
			self._contents = stack_aux

	def enqueuer(self,e):
		self.reverse_stack()
		self._contents.push(e)
		self._reverse_stack()

	def dequeue(self):
		self.reverse_stack()
		dequeue_value = self._contents.pop()
		self._reverse_stack()

		return dequeue_value

	def first(self):
		self.reverse_stack()
		first_value = self._contents.top()
		self.reverse_stack()

		return first_value

	def is_empty(self):
		return self._size == 0

	def len(self):
		return self._size



def sot_stack(stack):
	pass
