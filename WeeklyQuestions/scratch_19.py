w = 1
x = 6
result = list(map(lambda x: 2 ** x, range(x)))

for i in range(x):
 print("2 raised to the power of",i,"is",result[i])


x = 2
y = 0
z = 0
while w == 1:
    inp = input('Enter for exponent of 2')
    w = 2
    if inp == '':
        z = (x * x * y)
        y = y + 1
        print(x, '*', y, '=', z)
        w = 1

