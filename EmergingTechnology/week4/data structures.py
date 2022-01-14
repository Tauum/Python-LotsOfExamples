import json
from colorama import Fore

#list - mutible
list1 = [1,2,3, "y", True, 3.4]
print(list1[3])
list1.append(False)
list1[0] = 1
list1.pop()
list1.remove(2)
list1.insert(0,100) # < index, value


#array - immutible
array1 = (1,2,3)
#set - immutible

#tuple - immutible

#dictionary mutible
dictionary1 = {
    "id" : "100",
    "fname" : "bob",
    "lname" : "timer"
}
dictionary2 = {
    "id" : "001",
    "fname" : "bob",
    "lname" : "remit"
}
print(dictionary1)
print (type(dictionary1))
print(dictionary2)
dictionary2 |= dictionary1
print(dictionary1)


# a list of dictionaries
students = []
val_iter = 210000
choice = ""
while not choice == "N":
    choice = input("Y/N").upper()
    fname = input(f"forename for student with id {val_iter}").strip().capitalize() # strip removes whitespaces
    lname = input(f"lastname for student with id {val_iter}").strip().capitalize()
    new_student ={
        "id" : val_iter,
        "fname" : fname,
        "lname" : lname
    }
    val_iter += 1
    students.append(new_student)
    choice = input("Y/N").upper()

print(students)
            # V dumps is output dump is input
                # V object input
                            # V orders via id
                                            # V presentation
# V colours output
print(Fore.YELLOW)
print(json.dumps(students, sort_keys=True, indent=4))
print(Fore.RESET)