

#array - Provides compact array storage for primitive types.
#collections - involving collections of objects. Defines additional data structures and abstract base classes
#copy  Defines general functions for making copies of objects.
#heapq - Provides heap-based priority queue functions (see Section 9.3.7).
#math - Defines common mathematical constants and functions.
#os - Provides support for interactions with the operating system.
#random - Provides random number generation.
#re - Provides support for processing regular expressions.
#sys - Provides additional level of interaction with the Python interpreter.
#time - Provides support for measuring time, or delaying a program.

from math import pi, sqrt

class Lists:
	
	def __init(self):
		pass

	def minmax(self,list):
		min = list[0]
		max = list[0]
		for n in list:
			if n > max:
				max = n

			if n < min:
				min = n

		return min, max

	def soma(self,n):
		list = [sqrt(n) for n in range(0,n)]
		soma = 0
		for i in list:
			soma += i

		return soma

	def sumSaquareOdd(self,N):
		list = [ sqrt(2*n) for n in range(0,N/2)]
		soma = 0
		for i in list:
			soma += i

		return soma

	def product(self,N):
		for i in range(len(N)-1):
			if (N[i]*N[i+1]) % 2 == 0:
				return True

		return False

	def is_all_distinct(self,N):
		for i in range(len(N)-1):
			for j in range(i+1,len(N)):
				if N[i] == N[j]:
					return False

		return True
	
	def qtd_divide(self,n):
		if (n < 2):
			print "n can't be less than 2"
			return 0			

		qtd = 0
		while(n > 2):
			n = n/2
			qtd += 1

		return qtd
