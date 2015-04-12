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