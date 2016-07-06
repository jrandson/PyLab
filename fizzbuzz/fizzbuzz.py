'''

'''


def FizzBuzz(numero):
	if numero  % 15 == 0:
		return "fizzbuzz"

	if numero % 5 == 0:
		return "buzz"

	if numero % 3 == 0:
		return "fizz"

	return numero
