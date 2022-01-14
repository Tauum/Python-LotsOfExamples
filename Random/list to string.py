y = []
ylen = len(y)

def user_input():
    while True:
        uinp = (input('input: '))
        if uinp != 'no':
          y.append(uinp)
        elif uinp == 'no':
            return y
        
def user_con(y):
        ustr = ' '.join(str(x) for x in y)
        print('Output =',ustr)

user_input()
user_con(y)
