x = list(str(input('Enter number here:')))

print (x)

for i, row in enumerate(x):
    if '0' in row:
        print (row, 'Zero')
    elif '1' in row:
        print (row, 'One')
    elif '2' in row:
        print (row, 'Two')
    elif '3' in row:
        print (row, 'Three')
    elif '4' in row:
        print (row, 'Four')
    elif '5' in row:
        print (row, 'Five')
    elif '6' in row:
        print (row, 'Six')
    elif '7' in row:
        print (row, 'Seven')
    elif '8' in row:
        print (row, 'Eight')
    elif '9' in row:
        print (row, 'Nine')

