set = [['Index','Sex','Age','Height','Hip','BAI','Healthiness']]
tempset = []

counter = 0

def userinput():
    index = counter
    sex = input("M/F")
    age = int(input('age 20-79'))
    #height = float(input('height'))
    #hip = float(input('Hip'))
    height = 1.79
    hip = 90
    def BAIcalc(height, hip):
        return (lambda height, hip: (hip / (height) ** 1.5) - 18)(height, hip)
    BAI = BAIcalc(height, hip)
    BAIcalc(height, hip)
    print(BAI)
    if BAI < 8:
        healthiness = 'Underweight'
    elif BAI > 8:
        healthiness = 'Healthy'
    tempset = [index,sex,age,height,hip,BAI,healthiness]
    extendSet(set,tempset)
    return userinput()

def extendSet(set,tempset):
    #set.extend([[index,sex,age,height,hip,BAI,Healthiness]])
    set.extend([[tempset]])
    print(set)
    return input()

userinput()