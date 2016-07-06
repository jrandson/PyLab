import random as rand

def find(lista, n, low, high):

	mid = (high + low) // 2

	if low > high:
		return -1

	if n == lista[mid]:
		return mid

	if n > lista[mid]:
		return find(lista,n,mid+1,high)
	else:
		return find(lista,n,low, mid-1)

def soma_recursiva(data,n):
	if n == 0:
		return 0
	else:
		return soma_recursiva(data,n-1) + data[n-1]
	
def revert_sequence(str):
	if len(str) == 1:
		return str	
	last = len(str)-1	
	return str[last] + revert_sequence(str[0:last])

def power(x,n):
	if n == 0:
		return 1
	else:
		return x*power(x,n-1)

def get_max(data,n):
	
	if n == 1:
		return data[n-1]

	maxNumber = get_max(data,n-1)

	if maxNumber > data[n-1]:
		return maxNumber
	else:
		return data[n-1]

def get_min(data,n):
	if n == 1:
		return data[0]

	min_number = get_min(data,n-1)
	if min_number < data[n-1]:
		return min_number
	else:
		return data[n-1]

def produto(m,n):
	if n == 1:
		return m
	else:
		return m + produto(m,n-1)

def log(m,b):
	if m == 1:
		return 0

	if m == b:
		return 1
	else:
		m = m/b
		return 1 + log(m,b)
def is_palindrome(str,begin,end):
	if len(str) == 1:
		return True

	if begin + 2 < end:
		return is_palindrome(str,begin+1,end-1)		
	else:
		if str[begin] == str[end]:
			return True
		else:
			return False

def has_more_vowels_than_conoants(str,n):
	
	if n == 1:
		if str[0] in ['a','e','i','o','u']:
			return 1
		else:
			return 0

    


def teste_soma():
	data = [1,3,5,7,4,8]
	print soma_recursiva(data,6)

def test1():
	l = [int(rand.random()*100) for i in range(0,20)]
	l.sort()
	print l

	high = len(l)-1
	low = 0

	print find(l,50,high,low)
