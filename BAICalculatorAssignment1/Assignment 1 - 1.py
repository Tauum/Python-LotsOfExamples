import statistics
#input/error handling
error = 'Incorrect, Enter correct (format/value)'
na = 'N/A'
indexx = int()
hcm = float()
hmm = str()
#data
index = [0,1,2,3,4,5]
sex = ['F','M','F','M','F','M']
age = [21,42,36,27,46,31]
height = [1.72,1.91,1.423,1.685,1.620,1.854]
hip = [76.,99.3,63.5,82.55,94.488,100.838]
BAI = []
#avgdata
avgHeight = [175.3, 161.3]
avgHip = [37,27]
avgSex = ['M','F']
avgF = [21,33,39,23,35,41,25,38,43]
avgM = [8, 21,26,11,23,29,3,25,31]
ageBound = [[20,39],[40,59],[60.79]]
#setresults
setrange = []
setmean = []
setmode = []

def menu():
    clear()
    print('BAI - Body Adiposity Index (calculates healthiness based on body measurements)'
          '\n''\n1. Input data.\n2. Amend & View set data.\n3.'
          ' BAI calculation.\n4. View Average & Set results.\n5. Exit')
    input1 = input('Input (1,2,3,4,5): ')
    if input1 == '1':
        inputMenu()
        return
    elif input1 == '2':
        amendMenu()
        return
    elif input1 == '3':
        baiMenu(index, indexx)
    elif input1 == '4':
        avgsetResult()
        return
    elif input1 == '5':
        print('l8r sk8r')
        exit()
    else:
        print(error)
        menu()
        return error

def inputMenu():
    clear()
    indexSel(index)
    sexInput(sex, indexx)
    ageInput(age, indexx)
    heightInput(height, indexx)
    hipInput(hip, indexx)
    print('\n',indexx, '- added. Total index:',index)
    inputmenu = input('\nEnter to continue.')
    if inputmenu == '':
        menu()
        return
    else:
        menu()
        return

def indexSel(index):
    global indexx
    print('Index:',index)
    indexx = len(index)
    index.append(indexx)
    return

def sexInput(sex, indexx):
    input4 = input('Sex? (y/n): ').upper()
    if input4 == 'Y':
        hm1 = str(input('Sex (M/F): ')).upper()
        if hm1 == 'M':
            sex.insert(indexx, hm1)
            return
        elif hm1 == 'F':
            sex.insert(indexx, hm1)
            return
        else:
            print(error)
            sexInput(sex, indexx)
        return
    elif input4 == 'N':
        sex.insert(indexx, na)
        return
    else:
        print(error)
        sexInput(sex, indexx)
        return

def ageInput(age, indexx):
    input5 = input('Input age? (y/n): ').upper()
    if input5 == 'Y':
        hc7 = input('Age (20-79): ')
        if hc7.isdigit() == True:
            hc7 = int(hc7)
            if hc7 >= 20 and hcm <= 79:
                age.insert(indexx, hc7)
                return
        else:
            print(error, 'entry removed')
            ageInput(age, indexx)
    elif input5=='N':
        age.insert(indexx, na)
        return
    else:
        print(error)
        return ageInput(age, indexx)

def heightInput(height, indexx):
    inputhi1 = input('Height? (y/n): ').upper()
    if inputhi1 == 'Y':
        heightCalc(indexx, height)
        return
    elif inputhi1 == 'N':
        height.insert(indexx, na)
        return
    else:
        print(error)
        heightInput(height, indexx)
    return

def heightCalc(indexx, height):
    inputhc1 = input('1.Meters.\n2.feet.\n3.inches? \n(1,2,3): ')
    if inputhc1 == '1':
        hc = input('M (0.5-3): ')
        if hc.isdigit() == True or hc.isdecimal() == True:
            hc = float(hc)
            if hc > 0.4 and hc < 3:
                height.insert(indexx, hc)
                return
        else:
            print(error, 'entry removed')
            heightInput(height, indexx)
    elif inputhc1 == '2':
        hc = input('feet (3-8): ')
        if hc.isdigit() == True:
            hc = float(hc)
            if hc > 3 and hc < 8:
                hc2 = hc / 0.3048
                height.insert(indexx, hc2)
                return
        else:
            print(error, 'entry removed')
            heightInput(height, indexx)
    elif inputhc1 == '3':
        hc = input('inches (35-100): ')
        if hc.isdigit() == True:
            hc = float(hc)
            if hc > 35 and hc < 100:
                hc3 = hc * 0.0254
                height.insert(indexx, hc3)
                return
        else:
            print(error, 'entry removed')
            heightInput(height, indexx)
    else:
        print(error)
        heightCalc(indexx, height)

def hipInput(hip, indexx):
    input3 = input('Hip circumference? (y/n): ').upper()
    if input3 == 'Y':
        hipCalc(hip, indexx)
        return
    elif input3 == 'N':
        hip.insert(indexx, na)
        return
    else:
        print(error)
        hipInput(hip, indexx)
    return

def hipCalc(hip, indexx):
    input31 = input('1.Meters.\n2.feet.\n3.inches? \nInput(1,2,3): ')
    if input31 == '1':
        hc = input('M (0-2): ')
        if hc.isdigit() == True:
            hc = float(hc)
            if hc > 0 and hc < 2:
                hc = hc * 100
                hip.insert(indexx, hc)
                return
        else:
            print(error, 'entry removed')
            hipInput(hip, indexx)

    elif input31 == '2':
        hc = input('feet (0-6): ')
        if hc.isdigit() == True:
            hc = float(hc)
            if hc > 0 and hc < 6:
                hc5 = hc * 0.3048
                hip.insert(indexx, hc5)
                return
        else:
            print(error, 'entry removed')
            hipInput(hip, indexx)

    elif input31 == '3':
        hc = input('inches (0-80): ')
        if hc.isdigit() == True:
            hc = float(hc)
            if hc > 0 and hc < 80:
                hc6 = hc * 0.0254
                hip.insert(indexx, hc6)
                return
        else:
            print(error, 'entry removed')
            hipInput(hip, indexx)
    else:
        print(error)
        hipCalc(hip, indexx)

def baiCalc(BAI, height, hip, indexx, n):
    try:
        a = height[n]
        a1 = a * 1.5
        b = hip[n]
        c1 = b / a1
        c2 = c1 - 18
        c2 = round(c2,2)
        BAI.insert(n, c2)

        a = round(a,2)
        a1 = round(a1, 2)
        b = round(b,2)
        c1 = round(c1,2)
        print('index:',n,' height:',a,'*1.5=',a1,'hip:', b, 'hip/height=',c1,'-18 =',c2)
        return
    except:
        print('BAI calculation missing required data at index:',indexx, '.Please amend value/s in amend menu.')
        BAI.insert(indexx, na)
        return

def amendMenu():
    clear()
    input10 = input('1.Amend Data.\n2.View Data\n3.Return Main menu\nInput(1,2,3): ')
    if input10 == '1':
        amendEntry(index, height, hip, sex, age, BAI)
    elif input10 == '2':
        print('\nIndex: ',index,'\nHeight:',height,'\nHip:   ',hip,'\nSex:   ',sex,'\nAge:   ',age, '\nBAI:   ',BAI)
        input11 = input('\nEnter to return')
        if input11 =='':
            clear()
            return amendMenu()
        else:
            print(error)
            clear()
            return amendMenu()
    elif input10 == '3':
        clear()
        return menu()
    else:
        print(error)
        return amendMenu()

def amendEntry(index, height, hip, sex, age, BAI):
    inputae1 = input('\nData type?\n1.Total Index entry'
                        '\n2.Height \n3.Hip \n4.Sex\n5.Age\n6.Return\n(if data amended BAI must be recalculated) '
                     '\nInput(1,2,3,4,5,6): ')
    if inputae1 == '1':
        print('Index: ',index)
        indexx = int(input('Index select removal: '))
        del index[indexx]                                                   #if removed not 10 to 1 index order breaks
        del height[indexx]
        del hip[indexx]
        del sex[indexx]
        del age[indexx]
        BAI.clear()
        print('Total Index removed.')
        return amendEntry(index, height, hip, sex, age, BAI)

    elif inputae1 == '2':
        print('Index:', index)
        print('Height: ', height)
        indexx = int(input('Index replace:'))
        del height[indexx]
        BAI.clear()
        heightInput(height, indexx)
        return amendEntry(index, height, hip, sex, age, BAI)

    elif inputae1 == '3':
        print('Index:', index)
        print('Hip: ', hip)
        indexx = int(input('Index replace: '))
        del hip[indexx]
        BAI.clear()
        hipInput(hip, indexx)
        return amendEntry(index, height, hip, sex, age, BAI)

    elif inputae1 == '4':
        print('Index:', index)
        print('Sex: ', sex)
        indexx = int(input('Index replace: '))
        del sex[indexx]
        sexInput(sex,indexx)
        return amendEntry(index, height, hip, sex, age, BAI)

    elif inputae1 == '5':
        print('Index:', index)
        print('Age: ', age)
        indexx = int(input('Index select?'))
        del age[indexx]
        ageInput(age, indexx)
        return amendEntry(index, height, hip, sex, age, BAI)

    elif inputae1 == '6':
        clear()
        return amendMenu()
    else:
        print(error)
        return amendEntry(index, height, hip, sex, age, BAI)

def avgsetResult():
    clear()
    input15 = input('1.Average results.\n2.Set results.\n3.Return Main menu\nInput(1,2,3): ')
    if input15 == '1':
        averageResult(avgHeight, avgHip, avgSex,avgF,avgM)
    elif input15 == '2':
        #setResult()
        return avgsetResult()
    else:
        print(error)
        return avgsetResult()

def averageResult(avgHeight,avgHip,avgSex,avgF,avgM):
    inputar1 = input('\n1.Female?\n2.Male\n3.Return\nInput(1,2,3): ')
    if inputar1 == '1':
        print('\nAverage height: ', avgHeight[1],'Cm', '\nAverage Hip: ', avgHip[1],'Cm''\nSex:', avgSex[1],'\n')
        inputar2 = input('Age range: \n1.(20-39)\n2.(40-59)\n3.(60-79))\nInput(1,2,3): ')
        if inputar2 == '1':
            print('\nage range 20-39:')
            print('\nUnderweight is up to', avgF[0],'%.','\nHealthy is',avgF[0],'%','to',
                  avgF[1],'%.', '\nOverweight is',avgF[1],'%','to' ,avgF[2],'%.',
                  '\nObese is', avgF[2],'%','and greater.')
            return averageResult(avgHeight,avgHip,avgSex,avgF,avgM)

        elif inputar2 == '2':
                print('\nage range 40-59:')
                print('\nUnderweight is up to', avgF[3], '%.', '\nHealthy is', avgF[3],'%', 'to',
                      avgF[4],'%.', '\nOverweight is', avgF[4], '%', 'to', avgF[5],'%.',
                      '\nObese is', avgF[5],'%', 'and greater.')
                return averageResult(avgHeight, avgHip, avgSex, avgF, avgM)
        elif inputar2 == '3':
            print('\nage range 60-79:')
            print('\nUnderweight is up to', avgF[6], '%.', '\nHealthy is', avgF[6],'%', 'to',
                  avgF[7],'%.', '\nOverweight is', avgF[7], '%', 'to', avgF[8],'%.',
                  '\nObese is', avgF[8],'%.', 'and greater.')
            return averageResult(avgHeight, avgHip, avgSex, avgF, avgM)
        else:
            print(error)
            return averageResult(avgHeight, avgHip, avgSex, avgF,avgM)
    elif inputar1 == '2':
        print('\nAverage height: ', avgHeight[0],'Cm', '\nAverage Hip: ', avgHip[0],'Cm,''\nSex:', avgSex[0],'\n')
        inputar3 = input('Age range: \n1.(20-39)\n2.(40-59)\n3.(60-79))\nInput(1,2,3): ')
        if inputar3 == '1':
            print('\nage range 20-39:')
            print('\nUnderweight is up to', avgM[0],'%.','\nHealthy is',avgM[0],'%','to',
                  avgM[1],'%.', '\nOverweight is',avgM[1],'%','to' ,avgM[2],'%.',
                  '\nObese is', avgM[2],'%','and greater.')
            return averageResult(avgHeight, avgHip, avgSex, avgF, avgM)

        elif inputar3 == '2':
                print('\nage range 40-59:')
                print('\nUnderweight is up to', avgM[3],'%.', '\nHealthy is', avgM[3],'%', 'to',
                      avgM[4],'%.', '\nOverweight is', avgM[4], '%', 'to', avgM[5],'%.',
                      '\nObese is', avgM[5],'%', 'and greater.')
                return averageResult(avgHeight, avgHip, avgSex, avgF, avgM)
        elif inputar3 == '3':
            print('\nage range 60-79:')
            print('\nUnderweight is up to', avgM[6],'%.', '\nHealthy is', avgM[6],'%', 'to',
                  avgM[7],'%.', '\nOverweight is', avgM[7],'%', 'to', avgM[8], '%.',
                  '\nObese is', avgM[8],'%.', 'and greater.')
            return averageResult(avgHeight, avgHip, avgSex, avgF, avgM)
        else:
            print(error)
            return averageResult(avgHeight, avgHip, avgSex, avgF,avgM)
    elif inputar1 == '3':
        return menu()


def baiMenu(index, indexx):
                                                                  # doesnt return error if entry n/a
    input10 = input('\n1.Calculate Set BAI\n2.Return Main menu\nInput(1,2): ')
    if input10 =='1':
        BAI.clear()
        n = 0
        j = 0
        for x in index:
            baiCalc(BAI, height, hip, indexx, n)
            n += 1
            j += 1
        print('BAI:', BAI)
        if j >= 1:
            try:                                                #doesnt skip if n/a and crashes
                setIndex(setrange)
                setHeight(setmean, setrange, setmode)
                setHip(setmean, setrange, setmode)
                setAge(setmean, setrange, setmode)
                setBAI(setmean, setrange, setmode)
                return baiMenu(index, indexx, )
            except ValueError:
                    print('Set Error. Amend data')
                    return baiMenu(index, indexx )
        else:
            print('\nError while calculating BAI')
            return baiMenu(index, indexx )
    elif input10 == '2':
        return menu()
    else:
        print(error)
        return baiMenu(index, indexx)

def setIndex(setrange):
    indexset = index.copy()
    indexrange = indexset[-1] - indexset[0]
    setrange.insert(0, indexrange)
    print('Index - Range:', setrange[0])

def setHeight(setmean, setrange, setmode):      #doesnt return error if n/a
                                                # needs median
    try:
        heightset = height.copy()
        heightset.sort()
        heightrange = heightset[-1] - heightset[0]
        heightrange = round(heightrange, 3)
        setrange.insert(1, heightrange)
        heightmean = sum(heightset) / len(heightset)
        heightmean = round(heightmean, 3)
        setmean.insert(0,heightmean)
        try:
            heightmode = (statistics.mode(heightset))
            setmode.insert(0, heightmode)
            print('Height - Range:', setrange[1], ' - Mean:', setmean[0], ' - Mode:', setmode[0])
        except ValueError:
            print('Height - Range:', setrange[1], ' - Mean:', setmean[0], ' - Mode: N/A')

    except ValueError:
        print('Set height error. Amend height data')
        return baiMenu(index, indexx)

def setHip(setmean, setrange, setmode):
    try:
        hipset = hip.copy()
        hipset.sort()
        hiprange = hipset[-1] - hipset[0]
        hiprange = round(hiprange, 3)
        setrange.insert(2, hiprange)
        hipmean = sum(hipset) / len(hipset)
        hipmean = round(hipmean, 3)
        setmean.insert(1,hipmean)
        try:
            hipmode = (statistics.mode(hipset))
            setmode.insert(1, hipmode)
            print('Hip - Range:', setrange[2], ' - Mean:', setmean[1], ' - Mode:', setmode[1])
        except ValueError:
            print('Hip - Range:', setrange[2], ' - Mean:', setmean[1], ' - Mode: N/A')

    except ValueError:
        print('Set hip error. Amend hip data')
        return baiMenu(index, indexx)

def setAge(setmean, setrange, setmode):
    try:
        ageset = age.copy()
        ageset.sort()
        agerange = ageset[-1] - ageset[0]
        agerange = round(agerange, 3)
        setrange.insert(3, agerange)
        agemean = sum(ageset) / len(ageset)
        agemean = round(agemean, 3)
        setmean.insert(2,agemean)
        try:
            agemode = (statistics.mode(ageset))
            setmode.insert(2, agemode)
            print('Age - Range:', setrange[3], ' - Mean:', setmean[2], ' - Mode:', setmode[2])
        except ValueError:
            print('Age - Range:', setrange[3], ' - Mean:', setmean[2], ' - Mode: N/A')

    except ValueError:
        print('Set age error. Amend age data')
        return baiMenu(index, indexx)

def setBAI(setmean, setrange, setmode):
    try:
        BAIset = BAI.copy()
        BAIset.sort()
        BAIrange = BAIset[-1] - BAIset[0]
        BAIrange = round(BAIrange, 2)
        setrange.insert(4, BAIrange)
        BAImean = sum(BAIset) / len(BAIset)
        BAImean = round(BAImean, 2)
        setmean.insert(3, BAImean)
        try:
            BAImode = (statistics.mode(BAIset))
            setmode.insert(3, BAImode)
            print('BAI - Range:', setrange[4], ' - Mean:', setmean[3], ' - Mode:', setmode[3])
        except ValueError:
            print('BAI - Range:', setrange[4], ' - Mean:', setmean[3], ' - Mode: N/A')

    except ValueError:
        print('Set BAI error. Amend age data')
        return baiMenu(index, indexx)

def clear():
    print('\n '*8)
    return

menu()

#program work way easier/better with classes for input, edit, calc & output
#more input try would fix input related errors