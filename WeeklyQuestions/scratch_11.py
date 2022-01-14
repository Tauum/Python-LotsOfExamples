x = list(str(input('Enter number here:')))

print (x)

for i, row in enumerate(x):
    if '0' in row:
        print (row, 'Zero')
    if '1' in row:
        print (row, 'One')
