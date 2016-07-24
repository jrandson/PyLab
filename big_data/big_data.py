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


def find_dor(p):	
	found = False

	for i in range(0,1000):
		if i == p or i == -1*p:
			found = True
			break

	return found
