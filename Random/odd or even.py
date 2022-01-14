stop = 'stop'
print ('If input is odd or even.')
x = 1
while x == 1:
    num = (input('Please enter a number:'))
    if (int(num) % 2) == 0:
        print(num," is Even")
    elif(int(num)% 3) ==0:
        print( num," is Odd")
    elif(num) == 'stop':
        x = 2
