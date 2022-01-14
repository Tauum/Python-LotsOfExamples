
def tryExample(userinp):

    try:
        userinp = int(userinp)
        x = isinstance(userinp,int)
        if x == True:
            if userinp >= 1 and userinp <= 5:
                return "worked"
    except:
        return "failed"


print(tryExample("y"))

print(tryExample(5))

print(tryExample(10))
