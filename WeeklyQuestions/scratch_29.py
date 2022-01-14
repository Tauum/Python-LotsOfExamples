def main_menu():
        print ('calculate the sum difference, product or quotient of two numbers')
        calcinput = input('Entry list (+, -, /, * :')
        val1 = int(input('Value 1: '))
        val2 = int(input('Value 2: '))

        if calcinput == '+':
            val_result = add_numbers(val1, val2)
            print('Result of addition is:', val_result)
        elif calcinput == '-':
            val_result = subtract_numbers(val1, val2)
            print('Result of subtraction is:', val_result)
        elif calcinput == '/':
            val_result = devide_number(val1, val2)
            print('Result of devide is:', val_result)
        elif calcinput == '*':
            val_result = times_number(val1, val2)
            print('Result of times is:', val_result)

def add_numbers(val1, val2):
    val_result = val1 + val2
    return val_result
def subtract_numbers(val1, val2):
    val_result = val1 - val2
    return val_result
def devide_number(val1, val2):
    val_result = val1 / val2
    return val_result
def times_number(val1, val2):
    val_result = val1 * val2
    return val_result
pass


main_menu()