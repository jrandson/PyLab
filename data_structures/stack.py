class Stack:

	def __init__(self,contents = []):
		self._contents = contents

	def get_contents(self):
		return self._contents
	
	def push(self, p):		
		self._contents.append(p)

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


	

