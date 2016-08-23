class Queue:

	def __init__(self,content = []):
		self._content = content

	def get_content(self):
		return self._content

	def enqueuer(self,e):
		self._content = [e] + self._content

	def dequeue(self):
		if self.len() > 0:
			return self._content.pop(0)
		else:
			return None

	def first(self):
		if self.len() > 0:
			return self._content[0]
		else:
			return None

	def is_empty(self):
		return len(self._content) == 0

	def len(self):
		return len(self._content)
