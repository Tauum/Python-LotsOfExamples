# Author : Joseph Saunderson
# Date : 02/11/2021
# Objective : List Comprehension

# Create a list
list1 = [1,2,3,4,5] 
# Create a new list with number to the power of 2 and print new list

list2 = [] # blank list
count = 0 # interator to keep trakc on index
for list_element in list1: #
    list2.append(list1 [count] ** 2) # adds item to list2
    count += 1
print (f'list2 {list2}')

# list comprehension structure => new_list = [express for member in iterable]

list3 = [i**2 for i in list1]
print (f'list3 {list3}')

# create a list with numbers between 1 and 100

list4 = [i for i in range(2,100)]
print (f'list4 {list4}')

# new_list = [expression for member in iterable (if conditional)]

list5 = [i for i in range(2,100) if i % 2 == 0]
print (f'list5 {list5}')

# new_list = [expression (if conditional) for member in iterable]

list6 = [i < 20 for i in range (100)]
print (f'list6 {list6}')

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)