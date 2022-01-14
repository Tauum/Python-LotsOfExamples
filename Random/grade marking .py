a1 = ('34%, fail')
a2 = ('39&, borderline fail')
a3 = ('49%, class 3 - satisfactory quality')
a4 = ('59%, class 2/ii - good quality')
a5 = ('69%, Class 2/i - very good')
a6 = ('84%, Class 1 - excellent quality')
a7 = ('100%, Class 1 - exceptional quality')

print('this is where you can see your grade feedback')
a = (int(input('please enter your grade percentile here: '))
     
if (a >= 0 and a <= 34):
      print(a, a1)
elif(a >= 35 and a <= 39):
    print(a, a2)
elif (a >= 40 and a <= 49):
    print(a, a3)
elif (a >= 50 and a <= 59):
    print(a, a4)
elif (a >= 60 and a <= 69):
    print(a, a5)
elif (a >= 70 and a <= 84):
    print(a, a6)
elif (a >= 85 and a <= 100):
    print(a, a7)
