class Person:
    def __init__(self, index, height, hip, sex, age):
        self.index = index
        self.height = height
        self.hip = hip
        self.sex = sex
        self.age = age

    def printData(self):
        print('Index = ', self.index, '\nHeight =  ', self.height, '\nWeight = ', self.hip, '\nSex = ', self.sex, '\nAge = ', self.age)


x = int(0)
index = []

p1 = Person(0, 180, 36, 'M', 21)
p2 = Person(1, 120, 28, 'F', 30)

p1.printData()
p2.printData()
