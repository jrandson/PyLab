
import unittest

from linked_list import LinkedList 

class LinkListTest(unittest.TestCase):

	def test_add_node(self):
		
		ll = LinkedList()
		self.assertEqual(True,ll.is_empty())
		self.assertEqual('',ll.show_elements())
		
		ll.add_node(10)
		self.assertEqual(False,ll.is_empty())
		self.assertEqual('10->',ll.show_elements())
	
		ll.add_node(8)
		ll.add_node(1)
		self.assertEqual('1->8->10->',ll.show_elements())

	def test_add_new_tail(self):
		ll = LinkedList()
		ll.add_node(10)
		ll.add_node(8)
		ll.add_new_tail(5)		
		self.assertEqual('8->10->5->',ll.show_elements())
		ll.add_node(6)
		self.assertEqual('6->8->10->5->',ll.show_elements())

	def test_top(self):
		ll = LinkedList()
		self.assertEqual(None,ll.top())
		ll.add_node(10)
		ll.add_node(8)
		ll.add_new_tail(5)
		self.assertEqual(8,ll.top())

	def test_pop(self):
		ll = LinkedList()
		self.assertEqual(None,ll.pop())
		self.assertEqual('',ll.show_elements())
		ll.add_node(10)
		ll.add_node(8)
		ll.add_new_tail(5)
		self.assertEqual(8,ll.pop())
		self.assertEqual('10->5->',ll.show_elements())

	def test_remove_node(self):
		ll = LinkedList()
		
		ll.add_node(10)
		ll.add_node(8)
		ll.add_node(12)
		ll.add_new_tail(5)

		self.assertEqual('12->8->10->5->',ll.show_elements())
		ll.remove_node(10)		
		self.assertEqual('12->8->5->',ll.show_elements())
		ll.remove_node(12)		
		self.assertEqual('8->5->',ll.show_elements())
		ll.remove_node(5)		
		self.assertEqual('8->',ll.show_elements())

	def test_remove_repeated_with_buffer(self):
		ll = LinkedList()
		
		ll.add_node(10)
		ll.add_node(8)
		ll.add_node(12)
		ll.add_node(8)
		self.assertEqual('8->12->8->10->',ll.show_elements())
		ll.remove_repeated_with_buffer()
		self.assertEqual('12->8->10->',ll.show_elements())
		ll.add_node(10)
		ll.add_node(12)
		ll.add_node(3)
		ll.remove_repeated_with_buffer()
		self.assertEqual('3->12->8->10->',ll.show_elements())

	def test_remove_repeated_wihtout_buffer(self):
		ll = LinkedList()

		ll.add_node(10)
		ll.add_node(8)
		ll.add_node(12)
		ll.add_node(8)
		self.assertEqual('8->12->8->10->',ll.show_elements())
		ll.remove_repeated_without_buffer()
		self.assertEqual('12->8->10->',ll.show_elements())
		ll.add_node(10)
		ll.add_node(12)
		ll.add_node(3)
		ll.remove_repeated_without_buffer()
		self.assertEqual('3->12->8->10->',ll.show_elements())

	def test_remove_repeated_wihtout_buffer(self):
		ll = LinkedList()

		ll.add_node(10)
		ll.add_node(8)
		ll.add_node(12)
		ll.add_node(3)
		ll.add_node(5)
		ll.add_node(7)
		
		self.assertEqual([3,12,8,10],ll.find_last_n(3))
		self.assertEqual([7,5,3,12,8,10],ll.find_last_n(1))
		self.assertEqual([10],ll.find_last_n(6))

	def test_soma(self):
		l1 = populate_liste(513)
		self.assertEqual('3->1->5->',l1.show_elements())
		self.assertEqual(513,get_number_from_list(l1))

		l2 = populate_liste(295)
		self.assertEqual('5->9->2->',l2.show_elements())
		self.assertEqual(295,get_number_from_list(l2))

		self.assertEqual('8->0->8->',soma_lista(l1,l2).show_elements())


	def test_add_sort(self):
		ll = LinkedList()
		self.assertEqual('3->',ll.add_sort(3))
		self.assertEqual('5->3->',ll.add_sort(5))		
		self.assertEqual('5->4->3->',ll.add_sort(4))
		self.assertEqual('5->4->3->1->',ll.add_sort(1))
		self.assertEqual('5->4->3->2->1->',ll.add_sort(2))

	def test_add_sort2(self):
		ll = LinkedList()
		self.assertEqual('3->',ll.add_sort2(3))
		self.assertEqual('3->5->',ll.add_sort2(5))		
		self.assertEqual('3->4->5->',ll.add_sort2(4))
		self.assertEqual('1->3->4->5->',ll.add_sort2(1))
		self.assertEqual('1->2->3->4->5->',ll.add_sort2(2))

def populate_liste(n):
	ll = LinkedList()
	for i in str(n):
		ll.add_node(i)

	return ll

def get_number_from_list(lista):
	n = ''
	node = lista._head
	while not node == None:
		n = str(node._element) + n
		node = node._next

	return int(n)

def soma_lista(l1, l2):
	n1 = get_number_from_list(l1)
	n2 = get_number_from_list(l2)

	n3 = n1 + n2

	l3 = populate_liste(n3)

	return l3



if __name__ == '__main__':
	unittest.main()

