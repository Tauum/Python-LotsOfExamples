# Author:
# Date 01/10/2021
"""
Objective: Use selection programming constructs and data
validation to develop a solution that will allow students
to enter the grades of three final year modules.
The system determine the classification of their degree using ACM6.
If the average is 40 - 50 -> Third Class Degree
If the average is 50 - 60 -> Second Class Degree - Division II
If the average is 60 - 70 -> Second Class Degree - Division I
If the average is 70 - 100 -> First Class Degree
https://www.bolton.ac.uk/assets/Uploads/Assessment-Regulations-for-Undergraduate-Programmes-2019-2020.pdf
page 14
"""

examplegrades = [[50,50,25],[32,15,15],[64,90,76],[34,52,41]]

grades = [[]]

modules = ["a","b","c"]
#
# print('Degree classification')
#
# start = input('start? (y)')
#
# if (start == 'y' or 'Y'):
#
#     menuinput = input('(1) input own\n(2) use example\n(3) exit')
#
#     if (menuinput == "1"):
#         print("1")
#         swe5206 = int(input("swe5206: "))
#         sec5201 = int(input("sec5201: "))
#         swe6203 = int(input("swe6203: "))
#
#         from numpy import mean
#         average = mean (swe5206 + sec5201 + swe6203) / 3
#         average = round(average,2)
#      #   average = sum(swe5206 + sec5201 + swe6203) / 3
#
#         if average >= 40 and average <= 49:
#             print(f"{average} is equal to third class")
#         if average >= 50 and average <= 59:
#             print(f"{average} is equal to second II class")
#         if average >= 60 and average <= 69:
#             print(f"{average} is equal to second I class")
#         if average >= 70:
#             print(f"{average} is equal to first class")
#         else:
#             print(f"{average} is fail")
#
#     elif (menuinput == 2):
#         print("2")
#     else:
#         exit
# else:
#     quit

print("The program will be used to determine your degree classification.")
continue_var = input("Would you like to continue (Y/N):")
if continue_var.upper() == "N":
    quit
else:
    var = input("Enter the grade for SWE6206: ")
    print(var.isnumeric())
    while not var.isnumeric():
        var = input("Error, enter value again")
    swe6206 = int(var)





# a = np.array([[1, 2], [3, 4]])
# np.mean(a)
# 2.5
# np.mean(a, axis=0)
# array([2., 3.])
# np.mean(a, axis=1)
# array([1.5, 3.5])