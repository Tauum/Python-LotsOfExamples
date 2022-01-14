#!/bin/python3

#python string
print("double quotes")
print ('single quotes')
print (""" multiline
multiline """)
print ("concattonation" + "concattonation")
print ("\n new line")

#math
print ("\n")
print ("math:")
print (50 + 50, "add")
print (50 - 50,  "subtract")
print (50 * 50,  "multiply")
print (50 / 50,  "devide")
print (50 + 50 - 50 * 50 / 50,  "everything above")
print (50 ** 50,  "exponent")
print ( 50 % 6,  "modulo")
print ( 50 // 6,  "number without leftovers")

# variables & methods
print ("\n")
quote = "variable"
print (quote, quote + "added 1")
print (len(quote), "len")
print (quote.upper(), "upper")
print (quote.lower(), "lower")

tom = "tom"
age = int(21)
grade = float(65.5)
sexy = True
print ("name (string)", tom, "age (int)", age, "grade (float)", "sexy?", sexy)
age += 1
print ("age increased by 1", age)
birthday = 1
age += birthday
print("birthday", age)

#functions
print("\n")
def who_am_i():
	name = "tom"
	age = 21
	print (" name: " + name + " age: " + str(age))
who_am_i()

#adding perameters
def add_onehundred(num):
	print (num + 100)
add_onehundred(100)

#adding multiple perameters
def add(x,y):
	print(x + y)
add(7, 7)
add(150, 150)

#using return

def multiply(x,y):
	return x * y
print(multiply(15,15))

def square_root(x):
	return x ** .5
print (square_root(64))

#boolean expressions
print("boolean:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9
print(bool1, bool2, bool3, bool4)
print(type(bool1))
bool5 = "True"
print(type(bool5))

#relational and boolean operators
greaterthan = 7 > 5
lessthan = 5 < 7
greaterthanequal = 7 >= 7
lessthanequal = 7 <= 7
print(greaterthan, lessthan, greaterthanequal, lessthanequal)
testand = (7 > 5) and (8 < 7)
testor = (7 > 5) or (5 < 7)
testnot = not True




