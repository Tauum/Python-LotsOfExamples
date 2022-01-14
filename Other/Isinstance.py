

height = input('CM (50-300):')

try:
    height = float(height)
    res = isinstance(height, float)
    if res == True:
        if height >=1 and height <=3:
            print(res, 'inputted')
        else:
            print(res, 'not inputted')
    else:
        print(res)
except ValueError:
    print('false')