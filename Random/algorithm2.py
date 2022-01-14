import numpy
#numlist= [1,3,1,2,1,4,4,15,9,15,20,22,22,20,23,40,41,24,56,56,56,56,21,1,15,12]

print("this is used to find information of a numberlist.")
print ("Insert the full list with spaces inbetween")

numlist = [int(x) for x in input().split()]
numlist.sort()
sumlist = sum(numlist)

print ("List:", numlist)
print (numlist)
print ("The total number is",sumlist)
print ("The average number is ", numpy.average(numlist))
print ("The lowest number is ", numlist[0])
print ("The highest number is ", numlist [-1])

