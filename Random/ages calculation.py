def menu ():
    print('Accept ages until 0.')
    choice = choiceContinue()
    if choice == 'Y':
        collectAges()
    else:
        return
    
def choiceContinue ():
    choice = str(input('Continue? (y/n):')).upper()
    print(choice)
    while choice != 'Y' and choice != 'N':
        choice = str(input('Invalid. Enter (y/n)')).upper()
    return choice

def collectAges():
    ages = []
    while True:
        ageValue = int(input('Enter age:'))
        if ageValue != 0:
            ages.append(ageValue)
        elif ageValue == 0:
            delete(ages)
    return ages

def lowestAge(ages):
    print('Lowest age: ', min(ages))
    return
def highestAge(ages):
    print ('Highest age: ', max(ages))
    return
def averageAge(ages):
    a = sum(ages)
    b = len(ages)
    c = a / b
    #print(a,b)
    print('Average age:', c)

def delete(ages):
    print(ages)
    deleteChoice = input('Remove entry? (y/n)').upper()
    if deleteChoice == 'Y':
        z = int(input('Enter Value: '))
        ages.remove(z)
        finish(ages)
    else:
        finish(ages)

def finish(ages):
    print(len(ages), 'in set.')
    print('Values are:', end='')
    print(ages)
    lowestAge(ages)
    highestAge(ages)
    averageAge(ages)
    restart()

def restart():
    restart = input(('Restart? (y/n): ')).upper()
    if restart == 'Y':
        menu()
    else:
        exit()

menu()
