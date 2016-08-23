
import unittest

from queue import Queue 


class TestQueue(unittest.TestCase):

	def test_initialization(self):
		content = [1,4,3,5,7,6]
		
		queue = Queue()
		self.assertEqual([],queue.get_content())

		queue = Queue(content)
		self.assertEqual(content,queue.get_content())

	def test_enqueuer(self):
		queue = Queue()
		queue.enqueuer(10)
		self.assertEqual([10],queue.get_content())
		queue.enqueuer(8)
		self.assertEqual([8,10],queue.get_content())

	def test_dequeuer(self):
		content = [1,4,3,5,7,6]
		queue = Queue(content)
		self.assertEqual(1,queue.dequeue())
		self.assertEqual([4,3,5,7,6],queue.get_content())

	def test_first(self):		
		content1 = []		
		queue = Queue(content1)
		self.assertEqual(None,queue.first())

		content2 = [1,4,3,5,7,6]
		queue = Queue(content2)
		self.assertEqual(1,queue.first())

		queue.dequeue()
		self.assertEqual(4,queue.first())

	def test_empty(self):
		content = [1,4]		
		queue = Queue(content)
		queue.dequeue()
		self.assertEqual(False,queue.is_empty())
		queue.dequeue()
		self.assertEqual(True,queue.is_empty())





if __name__ == '__main__':
	unittest.main()