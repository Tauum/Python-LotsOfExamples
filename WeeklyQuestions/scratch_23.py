a1 = int(input('Enter spacing limit: '))
a2 = ('Hello world')
x = a1
z = '   '
counter = 0
print(counter)
while counter <= a1:
    counter += 1
    x += 1
    print (z * x, a2, counter)
while counter >= 2:
    counter -= 1
    x -=1
    print(z * x, a2, counter)
