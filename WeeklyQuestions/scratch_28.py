a2 = ('Hello world')

a1 = int(input('Enter spacing limit(minimum is 12): '))
x = a1
counter = 0

while counter <= a1:
    counter += 1
    x += 1
    a3 = a2.center(x, '-')
    print (a3, counter)
while counter >= 2:
    counter -= 1
    x -=1
    a3 = a2.center(x, '-')
    print(a3, counter)

#please talk to me regarding 12 being the minimum & why counter loop break
