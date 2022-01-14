y = []

def user_input():
    while True:
        uinp = (input('input another (y/no): '))
        if uinp != 'no':
          uinp = int(input('input number:'))
          y.append(uinp)
          print(y)
        elif uinp == 'no':
            break

def user_con(y):
        ylen = len(y)
        y.sort()
        anslow = min(y)
        anshigh = max(y)
        ansavg = y / ylen
        print(anslow, anshigh, ansavg)
        print(y, ylen)
user_input()
user_con(y)

