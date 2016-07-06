#!/usr/bin/env python

'''
assert: base assert allowing you to write your own assertions
assertEqual(a, b): check a and b are equal
assertNotEqual(a, b): check a and b are not equal
assertIn(a, b): check that a is in the item b
assertNotIn(a, b): check that a is not in the item b
assertFalse(a): check that the value of a is False
assertTrue(a): check the value of a is True
assertIsInstance(a, TYPE): check that a is of type "TYPE"
assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR



'''


import unittest
from fizzbuzz import FizzBuzz 

class TestFizzBuzz(unittest.TestCase):
	
	def test_numero_simples(self):
		self.assertEqual(FizzBuzz(1),1)
		self.assertEqual(FizzBuzz(2),2)


	def test_fizz(self):
		self.assertEqual(FizzBuzz(3),"fizz")
		self.assertEqual(FizzBuzz(9),"fizz")

	def test_buzz(self):
		self.assertEqual(FizzBuzz(5),"buzz")
		self.assertEqual(FizzBuzz(10),"buzz")

	def test_fizz_buzz(self):
		self.assertEqual(FizzBuzz(15),"fizzbuzz")
		self.assertEqual(FizzBuzz(30),"fizzbuzz")


if __name__ == '__main__':
	unittest.main()