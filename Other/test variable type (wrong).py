
a = 3.142
b = 3
c = 'C'

def isFloat (value):
    try:
        float(value)
        print(value)
        return True
    except ValueError:
        return False

def isInt (value):
    try:
        int(value)
        print(value)
        return True
    except ValueError:
        return False
def isStr (value):
    try:
        str(value)
        print(value)
        return True
    except ValueError:
        return False

print('Float A:',isFloat(a),isFloat(b),'Float C:',isFloat(c))
print('Int A:',isInt(a),'Int B:',isInt(b),'Int C:',isInt(c))
print('String A:',isStr(a),'String B:',isStr(b),'String C:',isStr(c))

#print(isFloat('A: ', a, 'B: ', b, 'C:', c))
#print(isInt('A: ', a, 'B: ', b, 'C:', c))
#print(isStr('A: ', a, 'B: ', b, 'C:', c))


