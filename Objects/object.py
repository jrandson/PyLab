
def __main__():
	
	cc = CreditCard('John Doe', '1st Bank', '5612 2983 0912 9238', 1000.0)
	 
	option = get_option()

	print option

	while not option[0] == 5 :
		
		option = get_option()

		if option[0] < 0:
			print option[1]

def get_option():

		options = {0: "Insert money",
				   1: "make a debit buying", 
				   2: "Show credit", 
				   3: "show sellings", 
				   5: "exit"}

		for i in options.keys():
			print str(i) + ": " + options[i]
		

		key = int(raw_input("Escolha uma opcao: "))

		if not key in options.keys():
			return (-1,"Opcao invalida")

		option = (key, options[key])

		return option

class CreditCard():

	def __init__(self,customer, bank, acnt,limit):

		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		return self._customer

	def get_bank(self):
		return self._bank

	def  get_account(self):
		return self._account

	def get_limit(self):
		return self._limit

	def get_balance(self):
		return self._balance


	def charge(self, price):

		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True
	
	def make_payment(self, value):
		if self._balance >= value:
			self._balance -= value
			return True
		else:
			return False

	def invest(entrada,tx,t):
		montante = entrada
		for i in range(t-1):
			montante *= (1 + tx)
			montante += entrada

		return montante

#=========================teste====================================

if __name__ == __main__:

	wallet = []
	wallet.append(CreditCard('John Bowman','California Savings', '9832 2787 0238 21001', 4100))
	wallet.append(CreditCard('John Bowman','California Savings', '9832 2787 0238 21001', 1900))
	wallet.append(CreditCard('John Bowman','California Savings', '9832 2787 0238 21001', 3500))

	for val in range(1,17):
		wallet[0].charge(val)
		wallet[1].charge(2*val)
		wallet[2].charge(3*val)

	for c in range(3):
		print "Customer =" + wallet[c].get_customer()
		print "Bank =" + wallet[c].get_bank()
		print "Account =" + wallet[c].get_account()
		print "limit =" + str(wallet[c].get_limit())
		print "Balance =" + str(wallet[c].get_balance())

		while wallet[c].get_balance() > 100:
			wallet[c].make_payment(100)
			print "New balance = " + str(wallet[0].get_balance())
		
		print ""



