# NAME: Mihai Caramizoiu
# 01.10.2021
# This program will take in grades for each module and calculate what type for degree you will get.

from statistics import mean
import os
clear = lambda: os.system('cls') # Clears out the console.
clear()

#Creating lists as they will be used to create some messages without repeeting the lines in the code.
modules = ["SWE4201", "SWE4202" ,"SWE4203", "SWE4204"]
degree = ["First Class ","Second Class Division I ","Second Class Division II ","Third Class "]
module_grade = [] # Stores all grades
failed_modules =[] # Stores any failed module

# this function will take in 3 arguments and creates a personalised message if the user passes all modules.
def degree_function(average_grade, degree_selection):
        print(f"\nBased on your average of {average_grade} marks, you have achieved a {degree_selection}degree.")
        quit

# this function will check what the user has entered, if it`s not a number or not a valid number from 1 to 100 it will get an error notification, otherwise will return the number.
def grade(i):
    while True:
        try:
           check_input = int(input(i))
        except ValueError:
            print(f"\nWARNING not a valid input! \nPlease enter a valid number\n")
            continue
        if check_input >=1 and check_input <= 100:
            return check_input
        else:
            print(f"\nWARNING {check_input} is not a valid input!\nGrades can be only from 1 to 100. Please enter again! \n")
            continue

# Will check if there are any modules with marks under 40 and stores info about in a list.
def check_all_grades():
    max_range = 39
    for x in module_grade:
        if x <= max_range:
            index = module_grade.index(x)
            failed = modules[index]
            failed_modules.append(failed)
        else:
            continue

# goes trough the list of modules and asks user to input grade.
def module_grab_info():
    for x in modules:
        mod = f"Please enter the numerical grade for the {x} module:  "
        check_grade = grade(mod)
        module_grade.append(check_grade)
        #print(module_grade) #testingy


answer = None
while answer not in ("YES", "NO","Y", "N"):
    answer=input("This program is used to determine the class of degree awarded.\nWould you like to continue?  (Y/N)  --->   ").upper()
    if answer == "YES" or answer == "Y" or answer == "YEA":
        print("Let`s start!\n")
        module_grab_info()
        break
    elif answer == "No"  or answer == "N" or answer == "NOPE":
        print("Ok, Thank you for your time!")
        quit
    else:
        clear() # Clears out console, for better visuals.
        print("Please enter a valdi answer! like Y, N, YES, NO ....")

#If there are any failed modules it will inform the user about it and what module he needs to work on
#as the average grade can be over 40 but not for each module.
#if all modules have minimum 40 marks, it will display a personalised message.

check_all_grades()

if len(failed_modules) >= 1:
    avr = mean(module_grade) #can also be written as:  sum(module_grade) / len(module_grade)  # calculates the sum of all numbers in module_grade list and devide them by the total nr.
    print(f"\nYour average grade is {avr}, in order to get the degree you need to have minimum 40 marks for each module.\nPlease re-take exams for the following module(s):\n ")
    for m in failed_modules:
        print(f"Module: {m}")
else:
    avr = mean(module_grade) #can also be written as:  sum(module_grade) / len(module_grade)  # calculates the sum of all numbers in module_grade list and devide them by the total nr.
    if avr >= 70:
        i = degree[0]
        degree_function(avr, i)
    elif avr >= 60 and avr <=69:
        i = degree[1]
        degree_function(avr, i)