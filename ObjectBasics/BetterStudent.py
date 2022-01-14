from Student import Student

class BetterStudent(Student): #<<<< inherits all functions from regular student class

        # VVV this gives the better student more functionality than regular
        def do_task_4(self):
            print("doing task 4")

        def do_task_5(self):
            print("doing task 5")

        #VVV overriding the previous task to allow different functionality
        def do_task_1(self):
            print("doing task 1 and 6")