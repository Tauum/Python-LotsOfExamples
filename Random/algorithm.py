import numpy
print("this is used to find information of a numberlist")
#numlist= [1,3,1,2,1,4,4,15,9,15,20,22,22,20,23,40,41,24,56,56,56,56,21,1,15,12]
print ("insert numbers with spaces inbetween")
numlist = [int(x) for x in input().split()]

numlist.sort()
sumlist = sum(numlist)
print ("list")
print (numlist)
print ("the total number is")
print (sumlist)
print (" the average number is ")
print (numpy.average(numlist))
print (" the lowest number is ")
print (numlist[1])
print (" the highest number is ")
print (numlist [-1])

while True:
    input_x = int(input("# or 0 to reset"))
    if (input_x) == 0:
        print ("Goodbye")
        break
    print (input_x) + 1
    print (input_x)
