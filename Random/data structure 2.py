StudentList = []
Vowelcount = 0
StudentList[x] = 1
Vowel = ["a", "e", "i", "o", "u"]

ammount = input("Enter how many students are there:")
print ("Enter student names:")
for i in range(int(ammount)):
    n = input("name: ")
    StudentList.append(str(n))
    StudentList.sort()

    for i in range(len(StudentList)):
        StudentList [x] +=1
        for Student in StudentList:
         Vowelcount = Vowelcount + 1





print("ARRAY: ", StudentList)
print("VOWEL COUNT:", Vowelcount)