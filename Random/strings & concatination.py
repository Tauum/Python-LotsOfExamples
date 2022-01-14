y = []
counter = 0
no = 'no'
ylen = len(y)
ustr = str()

def user_input():
    while True:
        uinp = (input('input: '))

        if uinp != 'no':
          y.append(uinp)
        elif uinp == 'no':
            print(y)
            return

def user_con():
    ustr = y[0] + y[1]
    y.remove[1]
    print (ustr)

user_input()
user_con()
