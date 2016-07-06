
import unittest
from recursao import find
from recursao import revert_sequence
from recursao import power
from recursao import get_max
from recursao import get_min
from recursao import produto
from recursao import log
from recursao import is_palindrome




class test_recursao(unittest.TestCase):
	lista = [12, 20, 26, 29, 32, 39, 49, 50, 51, 53, 57, 58, 59, 62, 69, 79, 80, 85, 95]
	
	def test_number_exixst(self):		
		self.assertEqual(find(self.lista, 50, 0, 18),7)

	def test_number_bord(self):		
		self.assertEqual(find(self.lista, 12, 0, 18),0)
		self.assertEqual(find(self.lista, 95, 0, 18),18)

	#---------------------------------------------------------	
	def test_revert_sequnce(self):
		self.assertEqual(revert_sequence('a'),'a')
		self.assertEqual(revert_sequence('ab'),'ba')
		self.assertEqual(revert_sequence('abc'),'cba')
		self.assertEqual(revert_sequence('abcd'),'dcba')
		self.assertEqual(revert_sequence('abcde'),'edcba')

	def test_power(self):
		self.assertEqual(power(1,0),1)
		self.assertEqual(power(2,1),2)
		self.assertEqual(power(2,3),8)

	def test_get_max(self):		
		self.assertEqual(get_max([10],1),10)
		self.assertEqual(get_max([10,12],2),12)
		self.assertEqual(get_max([10,15,11],3),15)
		self.assertEqual(get_max([10,15,11,20,1,23,19,8],8),23)

	def test_get_min(self):		
		self.assertEqual(get_min([10],1),10)
		self.assertEqual(get_min([10,12],2),10)
		self.assertEqual(get_min([10,15,11],3),10)
		self.assertEqual(get_min([10,15,11,20,1,23,19,8],8),1)

	def test_produto(self):		
		self.assertEqual(produto(2,1),2)
		self.assertEqual(produto(2,3),6)

	def test_log(self):
		self.assertEqual(log(1,2),0)
		self.assertEqual(log(2,2),1)
		self.assertEqual(log(4,2),2)

	def test_is_palindrome(self):
		self.assertEqual(is_palindrome('a',0,0),True)
		self.assertEqual(is_palindrome('ab',0,1),False)
		self.assertEqual(is_palindrome('aa',0,1),True)
		self.assertEqual(is_palindrome('aba',0,2),True)
		self.assertEqual(is_palindrome('abb',0,2),False)
		self.assertEqual(is_palindrome('radebar',0,6),False)
		self.assertEqual(is_palindrome('racecar',0,6),True)
		self.assertEqual(is_palindrome('abcddcba',0,7),True)


if __name__ == '__main__':
	unittest.main()