
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

from double_end_queue import DoubleEndQueue 

class TestDoubleEndQueue(unittest.TestCase):	
	
	def test_initialization(self):
		content = []
		d_queue = DoubleEndQueue(content)
		self.assertEqual(content,d_queue.get_content())

		content = [1,2,4,3,6]
		d_queue = DoubleEndQueue(content)
		self.assertEqual(content,d_queue.get_content())
		

	def test_add_first(self):
		d_queue = DoubleEndQueue()
		d_queue.add_first(8)
		self.assertEqual([8],d_queue.get_content())

		content = [3,6]
		d_queue = DoubleEndQueue(content)
		d_queue.add_first(10)
		self.assertEqual([10,3,6],d_queue.get_content())
		

	def test_add_last(self):
		d_queue = DoubleEndQueue()
		d_queue.add_last(8)
		self.assertEqual([8],d_queue.get_content())

		content = [3,6]
		d_queue = DoubleEndQueue(content)
		d_queue.add_last(10)
		self.assertEqual([3,6,10],d_queue.get_content())

	def test_delete_first(self):
		content = [3,6]
		d_queue = DoubleEndQueue(content)
		d_queue.delete_first()
		self.assertEqual([6],d_queue.get_content())

		d_queue = DoubleEndQueue()
		d_queue.delete_first()
		self.assertEqual([],d_queue.get_content())

	def test_delete_last(self):
		content = [3,6]
		d_queue = DoubleEndQueue(content)
		d_queue.delete_last()
		self.assertEqual([3],d_queue.get_content())

		d_queue = DoubleEndQueue()
		d_queue.delete_last()
		self.assertEqual([],d_queue.get_content())

	def test_fist(self):
		d_queue = DoubleEndQueue()
		self.assertEqual(None,d_queue.first())

		content = [3,6]
		d_queue = DoubleEndQueue(content)		
		self.assertEqual(3,d_queue.first())

	def test_last(self):
		d_queue = DoubleEndQueue()
		self.assertEqual(None,d_queue.last())

		content = [3,6]
		d_queue = DoubleEndQueue(content)		
		self.assertEqual(6,d_queue.last())

	def test_is_empty(self):
		content = [3,6]
		d_queue = DoubleEndQueue(content)
		d_queue.delete_first()
		self.assertEqual(False,d_queue.is_empty())

		d_queue.delete_first()
		self.assertEqual(True,d_queue.is_empty())

	def test_len(self):
		pass




if __name__ == '__main__':
	unittest.main()