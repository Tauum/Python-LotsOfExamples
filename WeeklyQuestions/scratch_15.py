total = 0
x = 0
numinput = 0
y = 0
print('This will add numbers less than 100')
x = 1
while True:
    if x == 1:
            numinput = (int(input('Enter number:')))
            y = numinput
            x = 2

    if x == 2:
        if y <= 100:
            total = y + total
            print('oh no')
            print('numberlist =', y, 'total =', total)
            num = 1
        elif numinput>=100:
            print ('Total =' , total)
