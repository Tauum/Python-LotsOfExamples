index = 0
height = 1.8
hip = 91

def BAIcalc(height,hip):
    return (lambda height,hip: (hip / (height)**1.5)- 18) (height,hip)
res = BAIcalc(height,hip)
BAI.insert(choice,BAI)
BAIcalc(height,hip)
print(BAI)


def calcBAI(BAI, height, hip,choice):                                                       # calculates bai based on input

    a = height[choice]
    a2 = a ** 1.5
    b = hip[choice]
    c = b / a2
    c2 = c - 18
    c2 = round(c2, 2)
    BAI.insert(choice, c2)

    a2 = round(a2, 2)
    c = round(c, 2)
    print('\n\t--\tBAI calculation = Height:', a, '**1.5=', a2, 'hip:', b, 'hip/height=', c, '-18 =', c2,'\n')
    return

y = float()
def increment(y):
    return (lambda x: x+1)(y)
a = 100
print('a = ',a)
b = increment(a)
print('a after incrementing =',b)
increment(y)