w = 1
x = 2
y = 0
z = 0
counter = 0

while w == 1:
    inp = input('Enter for exponent of 2')
    w = 2
    if inp == '':
        z = (x * x * y)
        y = y + 1
        counter = counter + 1
        print(x, '*', y, '=', z)
        print(counter)
        w = 1
