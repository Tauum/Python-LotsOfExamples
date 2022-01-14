p = 'tavs6hant4'
print('You have 4 attempts to correctly enter the password')
attempt_1 = str(input('Password:'))
if attempt_1 == p:
    x = 1
else:
    print('Attempt 1 incorrect, please try again.')
    attempt_2 = str(input('Password:'))
    if attempt_2 == p:
        x = 1
    else:
        print('Attempt 2 incorrect, please try again.')
        attempt_3 = str(input('Password:'))
        if attempt_3 == p:
            x = 1
        else:
            print('Attempt 3 incorrect, please try again.')
            attempt_4 = input(str('Last attempt password:'))
            if attempt_4 == p:
                x = 1
            else:
                x = 2
if x == 1:
    print('password correct')
else:
    print('Entered password incorrectly too many times.')
