y = []


def user_input():
    while True:
        uinp = (input('input: '))
        if uinp != 'no':
          uinp = float()
          y.append(uinp)
        elif uinp == 'no':
            return y


def user_con(y):
    ylen = len(y)
    for i in range(0,ylen,1):
        ans = y[0] + y[1]
        y.pop[0]
        counter = int()
        counter +=1
        print(ans, ylen, counter)

        if y[-1] == '1':
            print('pass')
        else:
            print('fail')
user_input()
user_con(y)

