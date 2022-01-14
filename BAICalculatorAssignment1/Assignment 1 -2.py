import statistics
                                                                                        #globals
#input/error handling
error = 'Error, Incorrect (format/value)'
returned = 'Returned.'
entryRem = 'Input entry removed.'
na = 'N/A'
#data storage
index = [0,1,2]
sex = ['M','F','M']
age = [21,27,21,27]
height = [179,155,179]
hip = [91,71,91]
BAI = [20,17,20]
healthiness = []
border = ' -'*48

print('\n\t', border)                                                                  # entry message
print('\n\t  (-<===[  BAI - Body Adiposity Index (calculates healthiness based on body measurements)  ]===>-)\t\t')

def menu():                                                                            # Main menu
    choice = int()
    print('\n\t',border,'\n')
    menustr = ['---------[ Menu ]---------', '[1 - Input data         ]', '[2 - View input data    ]',
               '[3 - Amend data         ]', '[4 - View set results   ]', '[5 - BAI chart          ]'
        , '[6 - Restart            ]', '[7 - Exit               ]']
    for i in range(len(menustr)):
        print('\t\t\t''{:<50s}'.format(menustr[i]))

    input1 = input('\n\t\t--\tInput > ')
    if input1 == '1':                                                                 # input menu
        indexSel(index)
        sexInput(sex, choice)
        ageInput(age, choice)
        heightInput(height, choice)
        hipInput(hip, choice)
        calcBAI(BAI, height, hip, choice)
        return menu()
    elif input1 =='2':                                                                 # view inputted data
        print('\n\t',border)
        print('\n\t\tIndex:     ',index)
        print('\t\tSex:       ',sex)
        print('\t\tAge:       ',age)
        print('\t\tHeight(M): ',height)
        print('\t\tHip(CM):   ',hip)
        print('\t\tBAI(%):    ',BAI)
        return menu()
    elif input1 == '3':                                                                 # amend menu
        amendMenu(index, sex, age, height, hip, BAI)
        return menu()

    elif input1 =='4':                                                                # calculates & prints set results
        setResults(index, age, height, hip, BAI)
        return menu()

    elif input1 == '5': #BAI chart
        print('\n\t',border)
        print('\n\t\tFemale - Age groups (20-39) (40-59) (60-79)')
        print('\t\tUnderweight up to: 21, 23, 25. (%)\n\t\tHealthy up to:     33, 35, 38. (%)'
              '\n\t\tOverweight up to:  39, 41, 43. (%)\n\t\tObese over:        39, 41, 43. (%)')
        print('\n\t',border)
        print('\n\t\tMale - Age groups   (20-39) (40-59) (60-79)')
        print('\t\tUnderweight up to:  8, 11, 13. (%)\n\t\tHealthy up to:     21, 23, 25. (%)'
              '\n\t\tOverweight up to:  26, 29, 31. (%)\n\t\tObese over:        26, 29, 31. (%)')
        print('\n\t',border)
        intype = input('\n\t- - [Ent to return]')
        if intype == '':
            print('\t\t',returned)
            clear()
            return menu()
        else:
            print('\t\t',returned)
            clear()
            return menu()

    elif input1 == '6':                                                       # Restarts program clearing lists
        index.clear()
        sex.clear()
        age.clear()
        height.clear()
        hip.clear()
        BAI.clear()
        healthiness.clear()
        choice = 0
        return menu()

    elif input1 == '7':                                                                # exits program
        print('\t\tl8r sk8r')
        exit()
    else:
        print('\n\t\t',error,returned,'\n')# input error
        menu()
        return

def indexSel(index):                                                          # makes index global & ammends index list
    global choice
    choice = len(index)
    index.append(choice)
    return

def sexInput(sex,choice):                                                                       # user inputs sex
    print('\n\t',border,'\n')
    inSex = input("\t--\tSex - [M/F] > ").upper()
    if inSex == 'M' or inSex == 'F':
        sex.insert(choice,inSex)
        return
    else:
        print('\t\t',entryRem,error)
        return sexInput(sex, choice)

def ageInput(age, choice):                                                                      # user inputs age
    inAge = input("\t--\tAge - [20]-[79] > ")
    try:
        inAge = int(inAge)
        res = isinstance(inAge, int)
        if res == True:
            if inAge >= 20 and inAge <= 79:
                age.insert(choice, inAge)
                return
            else:
                print('\t\t',entryRem, error)
                return ageInput(age, choice)
    except ValueError:
        print('\t\t',entryRem,error)
        return ageInput(age, choice)

def heightInput(height, choice):                                                                # user inputs height
    intype = input("\t--\tHeight - [1 CM] [2 - Meters] [3 - feet] [4 - inches] > ")
    if intype == '1':
        inHeight = input('\t--\t[CM] [50]-[300] > ')                                            # height in cm
        try:
            inHeight = float(inHeight)
            res = isinstance(inHeight,float)
            if res == True:
                if inHeight >= 50 and inHeight <= 300:
                    inHeight = inHeight / 100
                    inHeight = round(inHeight,2)
                    height.insert(choice ,inHeight)
                    return
                else:
                    print('\t\t',entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
            print('\t\t',entryRem, error)
            return heightInput(height,choice)


    elif intype == '2':
        inHeight = input('\t--\t[Meters] [1]-[3] >')                                        # height in m
        try:
            inHeight = float(inHeight)
            res = isinstance(inHeight,float)
            if res == True:
                if inHeight >= 1 and inHeight <= 3:
                    inHeight = round(inHeight,2)
                    height.insert(choice,inHeight)
                    return
                else:
                    print('\t\t',entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
                print('\t\t',entryRem,error)
                heightInput(height,choice)

    elif intype == '3':
        inHeight = input('\t--\t[Feet] [3.2]-[8] > ')                                      # height in feet
        try:
            inHeight = float(inHeight)
            res = isinstance(inHeight, float)
            if res == True:
                if inHeight >= 3.2 and inHeight <= 8:
                    inHeight = inHeight * 0.3048                                              # incorrect value
                    inHeight = round(inHeight,2)
                    height.insert(choice,inHeight)
                    return
                else:
                    print('\t\t',entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
                print('\t\t',error, 'entry removed')
                heightInput(height,choice)

    elif intype == '4':
        inHeight = input('\t--\tinches [39]-[100] > ')                                       # height in inches
        try:
            inHeight = float(inHeight)
            res = isinstance(height,float)
            if res == True:
                if inHeight >= 39 and inHeight <= 100:
                    inHeight = inHeight * 0.0254
                    inHeight = round(inHeight,2)
                    height.insert(choice,inHeight)
                    return
                else:
                    print('\t\t',entryRem, error)
                    return heightInput(height,choice)
        except ValueError:
                print('\t\t',error, 'entry removed')
                heightInput(height,choice)
    else:
        print('\t\t',error)
        heightInput(height,choice)

def hipInput(hip,choice):                                                                   # input hip circumference
    intype = input("\t--\tHip - [1 CM] [2 - Meters] [3 - feet] [4 - inches] >")
    if intype == '1':
        inHip = input('\t--\t[CM] [38]-[200] > ')                                           # input in cm
        try:
            inHip = float(inHip)
            res = isinstance(inHip, float)
            if res == True:
                if inHip >= 38 and inHip <= 200:
                    inHip = round(inHip,2)
                    hip.insert(choice,inHip)
                    return
                else:
                    print('\t\t',entryRem, error)
                    return hipInput(hip,choice)
        except ValueError:
            print('\t\t',entryRem, error)
            return hipInput(hip,choice)

    elif intype == '2':
        inHip = input('\t--\t[M] [0.38]-[2] > ')                                            # input in m
        try:
            inHip = float(inHip)
            res = isinstance(inHip, float)
            if res == True:
                if inHip >= 0.38 and inHip <= 2:
                    inHip = inHip * 100
                    inHip = round(inHip,2)
                    hip.insert(choice,inHip)
                    return
                else:
                    print('\t\t',entryRem, error)
                    return hipInput(hip,choice)
        except ValueError:
            print('\t\t',entryRem,error)
            hipInput(hip,choice)

    elif intype == '3':
        inHip = input('\t--\t[Feet] [1.21]-[6.6] > ')                                    # input in feet
        try:
            inHip = float(inHip)
            res = isinstance(inHip,float)
            if res == True:
                if inHip >= 1.21 and inHip <= 6.6:
                    inHip = inHip * 30.48
                    inHip = round(inHip,2)
                    hip.insert(choice,inHip)
                    return
                else:
                    print('\t\t',entryRem, error)
                    return hipInput(hip,choice)
        except ValueError:
            print('\t\t',entryRem,error)
            hipInput(hip,choice)

    elif intype == '4':
        inHip = input('\t--\t[Inches] [15]-[79] > ')                                    # input in inches
        try:
            inHip = float(inHip)
            res = isinstance(inHip,float)
            if res == True:
                if inHip >= 15 and inHip <= 79:
                    inHip = inHip * 2.54
                    inHip = round(inHip,2)
                    hip.insert(choice,inHip)
                    return
                else:
                    print('\t\t',entryRem,error)
                    hipInput(hip,choice)
        except ValueError:
            print('\t\t',entryRem,error)
            hipInput(hip,choice)
    else:
        print('\t\t',error)
        hipInput(hip,choice)

def calcBAI(BAI, height, hip,choice):                                               # calculates bai based on input

    a = height[choice]
    b = hip[choice]
    def BAIcalc(a, b):
        return (lambda a, b: (b / (a) ** 1.5) - 18)(a, b)
    BAIcalc(a, b)
    res = BAIcalc(a, b)
    res = round(res,2)
    BAI.insert(choice, res)
    print('\n\t--\tBAI calculation =','(Hip:',b,'Cm / (Height)(**1.5):',a,'M -18 =',res,'%')
    return

def amendMenu(index, sex, age, height, hip, BAI):                                  # user can ammend inputted data here
    print('\n\t', border, '\n')
    menustr = ['---------[ Menu ]---------', '[1 - Remove Total entry ]', '[2 - Sex                ]',
               '[3 - Age                ]', '[4 - Height             ]', '[5 - Hip                ]'
        , '[6 - Return             ]']
    for i in range(len(menustr)):
        print('\t\t\t''{:<50s}'.format(menustr[i]))
    print('\n\t', border, '\n')
    intype = input('\t -- Input> ')
    if intype == '1':
        print('\n\t', border, '\n')
        print('\n\t\tIndex -',index)
        indexsel = input('\n\t- - [Select Index] ')                                                 # deletes total index
        try:
            indexsel = int(indexsel)
            res = isinstance(indexsel, int)
            if res == True:
                del index[indexsel]
                del age[indexsel]
                del height[indexsel]
                del hip[indexsel]
                del sex[indexsel]
                try:
                    del BAI[indexsel]
                    print('\t\tTotal Index removed.')
                    return amendMenu(index, sex, age, height, hip, BAI)
                except:
                    print('no BAI to delete')
                    print('\t\tTotal Index removed.')
                    return amendMenu(index, sex, age, height, hip, BAI)
        except:
            print('\n\t\t', error, returned, '\n')
            return amendMenu(index, sex, age, height, hip, BAI)

    elif intype == '2':
        print('\t\t',index)
        print('\t\t',sex)
        indexsel = input('\n\t- - [Select index] ')                          # replaces user sex
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
        print('\t\t',index)
        print('\t\t',age)
        indexsel = input('\n\t- - [Select index] ')                           # replaces user age
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
        print('\t\t',index)
        print('\t','(M)',height)
        indexsel = input('\n\t- - [Select index] ')                          # replaces user height
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
        print('\t\t',index)
        print('   ','(CM)',hip)
        indexsel = input('\n\t- - [Select index] ')                                # replaces user hip
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

def setResults(index, age, height, hip, BAI):                           # calculates & prints mean, mode & range, prints healthiness
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

    print('\n\t\tIndex: ', index, '\n\t\tAge:   ', age, '\n\t\tSex:   ', sex,
          '\n\t\tHeight:', height, '\n\t\tHip:   ', hip, '\n\t\tBAI:   ', BAI)
    print('\t\tRange: Index=', indexrange,'- Age=', agerange,' - Height=', heightrange,' - Hip=', hiprange,' - BAI=', bairange,)
    print('\t\tMean:  Index= N/A - Age=', agemean,' - Height=', heightmean,' - Hip=', hipmean,' - BAI=', baimean)
    print('\t\tMode:  Index= N/A - Age=', agemode,' - Height=', heightmode,' - Hip=', hipmode,' - BAI=', baimode,'\n')
    returnmenu = input('\n\t- - [Ent to return] ')
    if returnmenu == '':
        print(returned,'\n')
        return menu()
    else:
        print(returned,'\n')
        return menu()

def setCalc():                                                                              #calculates healthiness
    healthiness.clear()
    counter = 0
    for i in range (0,len(index),1):
        if sex[counter] == 'M':                                                             # male healthiness
            if age[counter] <= 39:
                if BAI[counter] < 8:
                    healthiness.insert(counter,'Underweight')
                    counter += 1
                elif BAI[counter] >= 8 and BAI[counter] <= 21:
                    healthiness.insert(counter,'Healthy')
                    counter += 1
                elif BAI[counter] > 21 and BAI[counter] <= 26:
                    healthiness.insert(counter,'Overweight')
                    counter += 1
                elif BAI[counter] > 26:
                    healthiness.insert(counter, 'Obese')
                    counter += 1

            elif age[counter] >= 40 and age[counter] <= 59:
                if BAI[counter] < 11:
                    healthiness.insert(counter,'Underweight')
                    counter += 1
                elif BAI[counter] >= 11 and BAI[counter] <= 23:
                    healthiness.insert(counter,'Healthy')
                    counter += 1
                elif BAI[counter] > 23 and BAI[counter] < 29:
                    healthiness.insert(counter,'Overweight')
                    counter += 1
                elif BAI[counter] > 29:
                    healthiness.insert(counter, 'Obese')
                    counter += 1

            elif age[counter] >= 60 and age[counter] <= 79:
                if BAI[counter] < 13:
                    healthiness.insert(counter,'Underweight')
                    counter += 1
                elif BAI[counter] >= 13 and BAI[counter] <= 25:
                    healthiness.insert(counter,'Healthy')
                    counter += 1
                elif BAI[counter] > 25 and BAI[counter] < 31:
                    healthiness.insert(counter,'Overweight')
                    counter += 1
                elif BAI[counter] > 31:
                    healthiness.insert(counter, 'Obese')
                    counter += 1


        elif sex[counter] == 'F':                                                           #female healthiness
            if age[counter] <= 39:
                if BAI[counter] < 21:
                      healthiness.insert(counter, 'Underweight')
                      counter += 1
                elif BAI[counter] >= 21 and BAI[counter] <= 33:
                     healthiness.insert(counter, 'Healthy')
                     counter += 1
                elif BAI[counter] > 33 and BAI[counter] <= 39:
                     healthiness.insert(counter, 'Overweight')
                     counter += 1
                elif BAI[counter] > 39:
                    healthiness.insert(counter, 'Obese')
                    counter += 1

            elif age[counter] >= 40 and age[counter] <= 59:
                if BAI[counter] < 23:
                    healthiness.insert(counter, 'Underweight')
                    counter += 1
                elif BAI[counter] >= 23 and BAI[counter] <= 35:
                    healthiness.insert(counter, 'Healthy')
                    counter += 1
                elif BAI[counter] > 35 and BAI[counter] < 41:
                    healthiness.insert(counter, 'Overweight')
                    counter += 1
                elif BAI[counter] > 41:
                    healthiness.insert(counter, 'Obese')
                    counter += 1

            elif age[counter] >= 60 and age[counter] <= 79:
                if BAI[counter] < 25:
                    healthiness.insert(counter, 'Underweight')
                    counter += 1
                elif BAI[counter] >= 25 and BAI[counter] <= 38:
                    healthiness.insert(counter, 'Healthy')
                    counter += 1
                elif BAI[counter] > 38 and BAI[counter] < 43:
                    healthiness.insert(counter, 'Overweight')
                    counter += 1
                elif BAI[counter] > 43:
                    healthiness.insert(counter, 'Obese')
                    counter += 1

    underweight = healthiness.count('Underweight')
    healthy = healthiness.count('Healthy')
    overweight = healthiness.count('Overweight')
    obese = healthiness.count('Obese')
    try:
        underpercent = underweight /len(healthiness) * 100
    except:
        underpercent = 'N/A'

    try:
        healthpercent = healthy /len(healthiness) * 100
    except:
        healthpercent = 'N/A'
    try:
        overpercent = overweight /len(healthiness) * 100
    except:
        overpercent = 'N/A'
    try:
        obepercent = obese /len(healthiness) * 100
    except:
        obepercent = 'N/A'
    print('\n\t', border, '\n')
    print('\t ------[  Set Result Breakdown ]------  ')
    print('\n\t\tHealthiness:',healthiness,'\n\t\tCount: - Underweight:', underweight,
          ' - Healthy:', healthy, ' - Overweight:', overweight, ' - Obese:', obese)
    print('\t\t Percentages:','- underweight:',underpercent,'%','- healthy:', healthpercent,'%',' - Overweight:',overpercent,'%',' - Obese:',obepercent,'%' )
    return

def clear():                                                                            # prints 8 lines to clear screen
    print('\n '*8)
    return

menu()                                                                                  #program start