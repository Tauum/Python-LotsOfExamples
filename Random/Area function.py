def main_menu():
    print('calculate area of shape')
    shapeinp = input('Entry list (s,t,r,c :')

    if shapeinp == 's':
        val1 = float(input('Enter size : '))
        val_result = square(val1)
        print('Square area is:', val_result)
        main_menu()
    elif shapeinp == 't':
        val1 = float(input('Side 1 : '))
        val2 = float(input('Side 2 : '))
        val_result = triangle(val1, val2)
        print('Triangle area is:', val_result)
        main_menu()

    elif shapeinp == 'r':
        val1 = float(input('Side 1 : '))
        val2 = float(input('Side 2 : '))
        val_result = rectangle(val1, val2)
        print('Rectangle area is:', val_result)
        main_menu()
        
    elif shapeinp == 'c':
        val1 = float(input('Enter Diameter : '))
        val_result = circle(val1)
        print('Circle area is:', val_result)
        main_menu()
    else:
        SystemExit

def square(val1):
    val_result = val1 * val1
    return val_result

def triangle(val1, val2):
    val1 = val1 * 0.5
    val2 = val2 * 0.5
    val3 = val1 * val2
    val3 = 2 * val3
    val_result = val3
    return val_result

def rectangle(val1, val2):
    val_result = val1 * val2
    return val_result

def circle(val1):
    val_result = (3.142 * val1) * val1
    return val_result
pass


main_menu()
