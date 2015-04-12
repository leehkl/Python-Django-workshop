#variables are dynamic
a = 1
b = 5
print a + b

#switches value in a and b
a, b = b, a
print a
print b

#lists
list1 = ["apple", 'grape', 5]
print list1
print list1[0]
list1[2] = 'pear'
print list1[2]

# tuples are immutable variables, however you can change the value in a list that is inside of a tuple
tup = ("apple", "pear", [1,2,3])
tup[2][0] = 5
print tup

#key value pairs
py_dict = {'key': 'value'}
print py_dict['key']

#for loop
list2 = ['apple', 'something', 'else']
for x in list2:
		print x

#while loop
x = 0
while x < 5:
	print x
	x += 1

#functions
x = 33
z = "This is global z"
def add(x, y):
	#introduces the global z in the local function's scope, but not common to use globals in python
	global z
	print z
	#this x only looks at the local scope
	print x + y

add(5, 3)	

#or operator 
def even_odd(z):
	if z % 2 == 0 or z % 2 == 3:
		print "%s is even!" % z
	else:
		print "%r is odd!" % z

even_odd(1)
even_odd(2)
even_odd(3)

#classes, methods are functions inside of classes
class BankAccount():
	#called dunderinit
	def __init__(self, balance):
		self.balance = balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount

susan = BankAccount(1000000)
print susan.balance
susan.deposit(1000000)
print susan.balance
susan.withdraw(1000000)
print susan.balance

#inheritance
class MinBalanceAccount(BankAccount):
	def __init__(self, balance, minimum_balance):
		BankAccount.__init__(self, balance)
		self.minimum_balance = minimum_balance
	def withdraw(self, amount):
		if self.balance - amount < self.minimum_balance:
			print "Sorry, min balance must be maintained"
		else:
			BankAccount.withdraw(self, amount)
bob = MinBalanceAccount(120, 100)
bob.withdraw(50)
