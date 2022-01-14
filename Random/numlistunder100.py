total = 0
x = 0
y = 0
print('add numbers less than 100, above 100 shows total')
x = 1
while x == 1:
    numinput = (int(input('Enter number:')))
    y = numinput
    total = total + y
    print (y)
    if numinput >= 100:
        x = 2


while x == 2:
    if numinput >= 100:
        print('Above 100, total:', total)
        break
