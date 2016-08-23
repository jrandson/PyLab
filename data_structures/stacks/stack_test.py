
'''
assert: base assert allowing you to write your own assertions
assertEqual(a, b): check a and b are equal
assertNotEqual(a, b): check a and b are not equal
assertIn(a, b): check that a is in the item b
assertNotIn(a, b): check that a is not in the item b
assertFalse(a): check that the value of a is False
assertTrue(a): check the value of a is True
assertIsInstance(a, TYPE): check that a is of type "TYPE"
assertRaises
'''

import unittest
from stack import Stack
from stack import MyQueue

class TestStack(unittest.TestCase):	

	def test_initialization(self):
		contents = [3,6,2,7,2]
		stack = Stack(contents)
		self.assertEqual(contents, stack.get_contents())

	def test_push(self):
		contents = [3,6,2,7,2]
		stack = Stack(contents)
		stack.push(5)
		self.assertEqual([3,6,2,7,2,5],stack.get_contents())

	def test_len(self):
		contents = [3,6,2,7,2]
		stack = Stack(contents)
		self.assertEqual(5,stack.len())
		stack.push(10)
		self.assertEqual(6,stack.len())

	def test_pop(self):
		contents = [3,6,2,7,2]
		stack = Stack(contents)
		self.assertEqual(2,stack.pop())
		self.assertEqual(4,stack.len())

	def test_top(self):
		contents = [3,6,2,7,2]
		stack = Stack(contents)
		self.assertEqual(2,stack.top())
		stack.pop()
		self.assertEqual(7,stack.top())

	def test_is_empty(self):
		contents = [3]
		stack = Stack(contents)
		self.assertEqual(False, stack.is_empty())
		stack.pop()
		self.assertEqual(True, stack.is_empty())



if __name__ == '__main__':
	unittest.main()


