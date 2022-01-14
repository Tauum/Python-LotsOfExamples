y = []
ylen = len(y)
uinp = str()

def user_input():
    while True:
        uinp = (input('input: '))
        if uinp != 'no':
          y.append(uinp)
        elif uinp == 'no':
            return uinp


def user_con(y):
    if y[-1] == '1':
        print('pass')
    else:
        print('fail')

user_input()
user_con(y)