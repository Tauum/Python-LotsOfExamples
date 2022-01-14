import statistics

#input/error handling
error = 'Error, Incorrect (format/value)'
returned = 'Returned.'
entryRem = 'Input entry removed.'
na = 'N/A'
#data storage
index = [0,1,2]
sex = ['F','M','F']
age = [27,21,29]
height = [155,179,161]
hip = [60,91,72]
BAI = [9,15,11]
healthiness = []

def menu():
    choice = int()
    print('BAI - Body Adiposity Index (calculates healthiness based on body measurements)'
          '\n''\n1. Input data.\n2. View input data. \n3. Amend data\n4. View set results.\n5. BAI chart.\n6. Restart.\n7. Exit')
    input1 = input('Input (1,2,3,4,5,6): ')
    if input1 == '1':
        indexSel(index)
        sexInput(sex, choice)
        ageInput(age, choice)
        heightInput(height, choice)
        hipInput(hip, choice)
        calcBAI(BAI, height, hip, choice)
        return menu()
    elif input1 =='2':
        print('\nIndex:  ',index)
        print('Sex:    ',sex)
        print('Age:    ',age)
        print('Height: ',height)
        print('Hip:    ',hip)
        print('BAI:    ',BAI)
        print('Choice: ',choice)
        return menu()
    elif input1 == '3':
        amendMenu(index, sex, age, height, hip, BAI)
        return menu()

    elif input1 =='4':
        setResults(index, sex, age, height, hip, BAI, healthiness)
        return menu()

    elif input1 == '5':
        print('\nFemale - Age groups (20-39) (40-59) (60-79)')
        print('Underweight up to: 21, 23, 25. (%)\nHealthy up to:     33, 35, 38. (%)'
              '\nOverweight up to:  39, 41, 43. (%)\nObese over:        39, 41, 43. (%)')

        print('\nMale - Age groups   (20-39) (40-59) (60-79)')
        print('Underweight up to:  8, 11, 13. (%)\nHealthy up to:     21, 23, 25. (%)'
              '\nOverweight up to:  26, 29, 31. (%)\nObese over:        26, 29, 31. (%)')
        intype = input('\nPress enter to return Menu')
        if intype == '':
            print(returned)
            clear()
            return menu()
        else:
            print(returned)
            clear()
            return menu()

    elif input1 == '6':
        index.clear()
        sex.clear()
        age.clear()
        height.clear()
        hip.clear()
        BAI.clear()
        healthiness.clear()
        choice = 0
        return menu()

    elif input1 == '7':
        print('l8r sk8r')
        exit()
    else:
        print('\n',error,returned,'\n')
        menu()
        return

def indexSel(index):
    global choice
    print('Index: ',index)
    choice = len(index)
    index.append(choice)
    return

def sexInput(sex,choice):
    inSex = input("Person's Sex? (m/f)").upper()
    if inSex == 'M' or inSex == 'F':
        sex.insert(choice,inSex)
        return
    else:
        print(entryRem,error)
        sexInput(sex, choice)
        return

def ageInput(age, choice):
    inAge = input("Person's Age? (20-79)")
    try:
        inAge = int(inAge)
        res = isinstance(inAge, int)
        if res == True:
            if inAge >= 20 and inAge <= 79:
                age.insert(choice, inAge)
                return
            else:
                print(entryRem, error)
                return ageInput(age, choice)
    except ValueError:
        print(entryRem,error)
        return ageInput(age, choice)

def heightInput(height, choice):
    intype = input("Person's height? - 1.CM - 2.Meters. - 3.feet. - 4.inches (1,2,3,4) ")
    if intype == '1':
        inHeight = input('CM (50-300):')
        try:
            inHeight = float(inHeight)
            res = isinstance(inHeight,float)
            if res == True:
                if inHeight >= 50 and inHeight <= 300:
                    inHeight = inHeight / 100
                    height.insert(choice ,inHeight)
                    return
                else:
                    print(entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
            print(entryRem, error)
            return heightInput(height,choice)


    elif intype == '2':
        inHeight = input('M (1-3):')
        try:
            inHeight = float(inHeight)
            res = isinstance(inHeight,float)
            if res == True:
                if inHeight >= 1 and inHeight <= 3:
                    height.insert(choice,inHeight)
                    return
                else:
                    print(entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
                print(entryRem,error)
                heightInput(height,choice)

    elif intype == '3':
        inHeight = input('feet (3.2-8):')
        try:
            inHeight = float(inHeight)
            res = isinstance(inHeight, float)
            if res == True:
                if inHeight >= 3.2 and inHeight <= 8:
                    inHeight = inHeight * 0.3048
                    height.insert(choice,inHeight)
                    return
                else:
                    print(entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
                print(error, 'entry removed')
                heightInput(height,choice)

    elif intype == '4':
        inHeight = input('inches (39-100): ')
        try:
            inHeight = float(inHeight)
            res = isinstance(height,float)
            if res == True:
                if inHeight >= 39 and inHeight <= 100:
                    inHeight = inHeight * 0.0254
                    height.insert(choice,inHeight)
                    return
                else:
                    print(entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
                print(error, 'entry removed')
                heightInput(height,choice)
    else:
        print(error)
        heightInput(height,choice)

def hipInput(hip,choice):
    intype = input("Person's hip? - 1.CM - 2.Meters. - 3.feet. - 4.inches (1,2,3,4) ")
    if intype == '1':
        inHip = input('CM (38-200):')
        try:
            inHip = float(inHip)
            res = isinstance(inHip, float)
            if res == True:
                if inHip >= 38 and inHip <= 200:
                    hip.insert(choice,inHip)
                    return
                else:
                    print(entryRem, error)
                    return hipInput(hip,choice)
        except ValueError:
            print(entryRem, error)
            return hipInput(hip,choice)

    elif intype == '2':
        inHip = input('M (0.38-2):')
        try:
            inHip = float(inHip)
            res = isinstance(inHip, float)
            if res == True:
                if inHip >= 0.38 and inHip <= 2:
                    inHip = inHip * 100
                    hip.insert(choice,inHip)
                    return
                else:
                    print(entryRem, error)
                    return hipInput(hip,choice)
        except ValueError:
            print(entryRem,error)
            hipInput(hip,choice)

    elif intype == '3':
        inHip = input('feet (1.21-6.6): ')
        try:
            inHip = float(inHip)
            res = isinstance(inHip,float)
            if res == True:
                if inHip >= 1.21 and hip <= 6.6:
                    inHip = inHip * 0.3048
                    hip.insert(choice,inHip)
                    return
                else:
                    print(entryRem, error)
                    return hipInput(hip,choice)
        except ValueError:
            print(entryRem,error)
            hipInput(hip,choice)

    elif intype == '4':
        inHip = input('inches (15-79): ')
        try:
            inHip = float(inHip)
            res = isinstance(inHip,float)
            if res == True:
                if inHip >= 15 and inHip <= 79:
                    inHip = inHip * 0.0254
                    hip.insert(choice,inHip)
                    return
                else:
                    print(entryRem,error)
                    hipInput(hip,choice)
        except ValueError:
            print(entryRem,error)
            hipInput(hip,choice)
    else:
        print(error)
        hipInput(hip,choice)

def calcBAI(BAI, height, hip,choice):

    a = height[choice]
    a2 = a * 1.5
    b = hip[choice]
    c = b / a2
    c2 = c - 18
    c2 = round(c2, 2)
    BAI.insert(choice, c2)

    a = round(a, 2)
    a2 = round(a2, 2)
    b = round(b, 2)
    c = round(c, 2)

    print('\nBAI calculation = Height:', a, '*1.5=', a2, 'hip:', b, 'hip/height=', c, '-18 =', c2,'\n')
    return

def amendMenu(index, sex, age, height, hip, BAI):               #doesnt return error if selecting out of range index
    print('\n Select data type: \n1. Remove total index\n2. Sex.\n3. Age\n4. Height.\n5. Hip\n6. Return Menu')
    intype = input('Input (1,2,3,4,5,6):')
    if intype == '1':
        print(index)
        indexsel = input('Index select:')
        try:
            indexsel = int(indexsel)
            res = isinstance(indexsel, int)
            if res == True:
                del index[indexsel]
                del height[indexsel]
                del hip[indexsel]
                del sex[indexsel]
                del age[indexsel]
                del BAI[indexsel]
                print('Total Index removed.')
                return amendMenu(index, sex, age, height, hip, BAI)
        except:
            print(entryRem, error)
            return amendMenu(index, sex, age, height, hip, BAI)

    elif intype == '2':
        print(index)
        print(sex)
        indexsel = input('Index select:')
        try:
            indexsel = int(indexsel)
            res = isinstance(indexsel,int)
            if res == True:
                del sex[indexsel]
                choice = indexsel
                sexInput(sex,choice)
                return amendMenu(index,sex,age,height,hip,BAI)
        except:
            print(entryRem, error)
            return amendMenu(index, sex, age, height, hip, BAI)
    elif intype == '3':
        print(index)
        print(age)
        indexsel = input('Index select:')
        try:
            indexsel = int(indexsel)
            res = isinstance(indexsel,int)
            if res == True:
                del age[indexsel]
                choice = indexsel
                ageInput(age,choice)
                return amendMenu(index,sex,age,height,hip,BAI)
        except:
            print(entryRem, error)
            return amendMenu(index, sex, age, height, hip, BAI)
    elif intype == '4':
        print(index)
        print(height)
        indexsel = input('Index select:')
        try:
            indexsel = int(indexsel)
            res = isinstance(indexsel,int)
            if res == True:
                del height[indexsel]
                del BAI[indexsel]
                choice = indexsel
                heightInput(height,choice)
                calcBAI(BAI, height, hip, choice)
                return amendMenu(index,sex,age,height,hip,BAI)
        except:
            print(entryRem, error)
            return amendMenu(index, sex, age, height, hip, BAI)
    elif intype == '5':
        print(index)
        print(hip)
        indexsel = input('Index select:')
        try:
            indexsel = int(indexsel)
            res = isinstance(indexsel,int)
            if res == True:
                del hip[indexsel]
                del BAI[indexsel]
                choice = indexsel
                hipInput(hip,choice)
                calcBAI(BAI, height, hip, choice)
                return amendMenu(index,sex,age,height,hip,BAI)
        except:
            print(entryRem, error)
            return amendMenu(index, sex, age, height, hip, BAI)
    elif intype == '6':
        return menu()


def setResults(index, sex, age, height, hip, BAI, healthiness):
    indexset = index.copy()
    ageset = age.copy()
    heightset = height.copy()
    hipset = hip.copy()
    baiset = BAI.copy()

    indexset.sort()
    ageset.sort()
    heightset.sort()
    hipset.sort()
    baiset.sort()
    try:
        indexrange = indexset[-1] - indexset[0]
    except:
        indexrange = 'N/A'
    try:
        agerange = ageset[-1] - ageset[0]
        agerange = round(agerange, 2)
    except:
        agerange = 'N/A'
    try:
        heightrange = heightset[-1] - heightset[0]
        heightrange = round(heightrange, 2)
    except:
        heightrange = 'N/A'
    try:
        hiprange = hipset[-1] - hipset[0]
        hiprange = round(hiprange, 2)
    except:
        hiprange = 'N/A'
    try:
        bairange = baiset[-1] - baiset[0]
        bairange = round(bairange, 2)
    except:
        bairange = 'N/A'
    try:
        agemean = sum(ageset) / len(ageset)
        agemean = round(agemean,2)
    except:
        agemean = 'N/A'
    try:
        heightmean = sum(heightset) / len(heightset)
        heightmean = round(heightmean,2)
    except:
        heightmean = 'N/A'
    try:
        hipmean = sum(hipset) / len(hipset)
        hipmean = round(hipmean,2)
    except:
        hipmean = 'N/A'
    try:
        baimean = sum(baiset) / len(baiset)
        baimean = round(baimean,2)
    except:
        baimean = 'N/A'
    try:
        agemode = (statistics.mode(ageset))
    except:
        agemode = 'N/A'
    try:
        heightmode = (statistics.mode(heightset))
    except:
        heightmode = 'N/A'
    try:
        hipmode = (statistics.mode(hipset))
    except:
        hipmode = 'N/A'
    try:
        baimode = (statistics.mode(baiset))
    except:
        baimode = 'N/A'
    try:
        setCalc()
    except:
        healthiness = 'N/A'

    print('\nRange: Index=', indexrange,'- Age=', agerange,' - Height=', heightrange,' - Hip=', hiprange,' - BAI=', bairange,)
    print('Mean:  Index= N/A - Age=', agemean,' - Height=', heightmean,' - Hip=', hipmean,' - BAI=', baimean)
    print('Mode:  Index= N/A - Age=', agemode,' - Height=', heightmode,' - Hip=', hipmode,' - BAI=', baimode,'\n')
    returnmenu = input('Press Enter to return')
    if returnmenu == '':
        print(returned,'\n')
        return menu()
    else:
        print(returned,'\n')
        return menu()

def setCalc():
    counter = 0
    print('\nIndex:', index, '\nAge:', age, '\nSex:', sex, '\nHeight:', height, '\nHip:', hip, '\nBAI:', BAI)
    for i in range (0,len(index),1):
        if sex[counter] == 'M':
            if age[counter] <= 39:
                if BAI[counter] < 8:
                    healthiness.insert(counter,'Underweight')
                elif BAI[counter] >= 8 and BAI[counter] <= 21:
                    healthiness.insert(counter,'Healthy')
                elif BAI[counter] > 21 and BAI[counter] <= 26:
                    healthiness.insert(counter,'Overweight')
                elif BAI[counter] > 26:
                    healthiness.insert(counter, 'Obese')

            elif age[counter] >= 40 and age[counter] <= 59:
                if BAI[counter] < 11:
                    healthiness.insert(counter,'Underweight')
                elif BAI[counter] >= 11 and BAI[counter] <= 23:
                    healthiness.insert(counter,'Healthy')
                elif BAI[counter] > 23 and BAI[counter] < 29:
                    healthiness.insert(counter,'Overweight')
                elif BAI[counter] > 29:
                    healthiness.insert(counter, 'Obese')

            elif age[counter] >= 60 and age[counter] <= 79:
                if BAI[counter] < 13:
                    healthiness.insert(counter,'Underweight')
                elif BAI[counter] >= 13 and BAI[counter] <= 25:
                    healthiness.insert(counter,'Healthy')
                elif BAI[counter] > 25 and BAI[counter] < 31:
                    healthiness.insert(counter,'Overweight')
                elif BAI[counter] > 31:
                    healthiness.insert(counter, 'Obese')


        elif sex[counter] == 'F':
            if age[counter] <= 39:
                if BAI[counter] < 21:
                      healthiness.insert(counter, 'Underweight')
                elif BAI[counter] >= 21 and BAI[counter] <= 33:
                     healthiness.insert(counter, 'Healthy')
                elif BAI[counter] > 33 and BAI[counter] <= 39:
                     healthiness.insert(counter, 'Overweight')
                elif BAI[counter] > 39:
                    healthiness.insert(counter, 'Obese')

            elif age[counter] >= 40 and age[counter] <= 59:
                if BAI[counter] < 23:
                    healthiness.insert(counter, 'Underweight')
                elif BAI[counter] >= 23 and BAI[counter] <= 35:
                    healthiness.insert(counter, 'Healthy')
                elif BAI[counter] > 35 and BAI[counter] < 41:
                    healthiness.insert(counter, 'Overweight')
                elif BAI[counter] > 41:
                    healthiness.insert(counter, 'Obese')

            elif age[counter] >= 60 and age[counter] <= 79:
                if BAI[counter] < 25:
                    healthiness.insert(counter, 'Underweight')
                elif BAI[counter] >= 25 and BAI[counter] <= 38:
                    healthiness.insert(counter, 'Healthy')
                elif BAI[counter] > 38 and BAI[counter] < 43:
                    healthiness.insert(counter, 'Overweight')
                elif BAI[counter] > 43:
                    healthiness.insert(counter, 'Obese')

    underweight = healthiness.count('Underweight')
    healthy = healthiness.count('Healthy')
    overweight = healthiness.count('Overweight')
    obese = healthiness.count('Obese')
    print('Healthiness: - Underweight:', underweight, ' - Healthy:', healthy, ' - Overweight:', overweight, ' - Obese:', obese)
    return

def clear():
    print('\n '*8)
    return

menu()


#print(set[0][1])

# x = 0
# x = int(input(' array select:'))
# y = int(input('index select:'))
# z = int(input('element input:'))
# tempset[x].insert(y,z)
# print(tempset)
