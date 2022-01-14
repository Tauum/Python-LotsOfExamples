y = []

def user_input():
    while True:
        uinp = (input('input another (y/no): '))
        if uinp != 'no':
          uinp = float(input('input number:'))
          y.append(uinp)
          print(y)
        elif uinp == 'no':
            break


def user_con(y):
    while True:
        ylen = len(y)
        sumy = sum(y)
        print(y, 'Length = ',ylen,'Total', sumy)
        break

user_input()
user_con(y)
