inlist = []

while True:
    print ('Enter int', end = '')
    inlist.append(str(input('here:')))

    print ('continue? (Y/N):', end = '')
    continueEnter = input().upper()

    if continueEnter == 'N':
        ustr = inlist[0] + inlist[1]
        ustr.split()
        print(ustr)
        break

print (inlist)