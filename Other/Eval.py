
height = eval(input('feet (3.2-8):'))
if type(height) == int or type(height) == float:
    height = float(height)
    if height >= 3.2 and height <= 8:
        height = height * 0.3048
        print(height)

if type(height)==float:
    print('is float')
else:
    print('not float')
if type(height)==int:
    print('is int')
else:
    print('not int')