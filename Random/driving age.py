age_o16 = ('You are above the legal age to drive')
age_u16 = ('You are not above the legal age to drive')

print('this is where you can see if youre legal to drive')
age = (int(input('Enter your age here: ')))
     
if age >= 15:
    print('Your age:', age, age_o16)
else:
    print ('Your age:', age, age_u16)
