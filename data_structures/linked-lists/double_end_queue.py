

class DoubleEndQueue:

	def __init__(self, content = []):
		self._content = content

	def get_content(self):
		return self._content


	def add_first(self, d):
		self._content = [d] + self._content

	def add_last(self, d):
		self._content.append(d)

	def delete_first(self):
		if self.len() > 0:
			self._content.pop(0)

	def delete_last(self):
		if self.len() > 0:
			self._content.pop()

	def first(self):
		if self.len() > 0:
			return self._content[0]

	def last(self):
		if self.len() > 0:
			return self._content[-1]

	def is_empty(self):
		return len(self._content) == 0

	def len(self):
		return len(self._content)