class Student:
    def __init__(self, name, major, grade):
        self.name = name
        self.major = major
        self.grade = grade

    def is_passed(self):
        if self.grade >= 50:
            return True
        else:
            return False

    def do_task_1(self):
        print("doing task 1")

    def do_task_2(self):
        print("doing task 2")

    def do_task_3(self):
        print("doing task 3")


student1 = Student("Tom S", "Computing", 58)
student2 = Student("Blake W", "Catering", 25)

print(student1.is_passed())
print(student2.is_passed())

