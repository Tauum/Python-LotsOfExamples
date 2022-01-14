from inputdef.py import
import

x = 0
error = 'Incorrect, Enter correct (format/value)'
returning = 'Returning...'
na = 'N/A'
nax = (na + str(x))
index = []
height = []
hip = []
sex = []
age = []
hcm = float()
hmm = float()

averageheight = [175.3, 161.3]
averagehip = [37,27]
averagesex = ['M','F']

setmean = float()
setmode = float()
setaverage = float()
setrange = float()


def menu(x):
    print('Body Adiposity Index (BAI)\n1. Input data.\n2. Amend/view data.\n3. View averages\n4. Set results.\n5. Comparison (Averages Vs. Set).')
    input1 = input('Input (1,2,3,4,5): ')
    if input1 == '1':
        inputMenu(x,)
        return
    elif input1 == '2':
        amendMenu(index, height, hip, sex, age, x)
        return
    elif input1 == '3':
        averageResult(averageheight, averagehip, averagesex)
        return
    elif input1 == '4':
        setResults(index, height, hip, sex, age, x)
        return
    elif input1 == '5':
        averageVsYours(averageheight, averagehip, averagesex, index, height, hip, sex, age, x)
    else:
        print(error)
        menu()
    return

def inputMenu(x):
    x +=1
    index.append(x)
    heightInput(height, hcm)
    hipInput(hip, hmm)
    sexInput(sex)
    ageInput(age)
    print('Data added, Current index:',index)
    menu(x)
    return

def amendMenu(index, height, hip, sex, age, x):
    input10 = input('Amend, view data or return? (1,2,3)').upper
    if input10 == 1:
        input11 = input('Data type?\n1.Total Index entry \n2.Height \n3.Hip \n4.Sex')
        if input11 == 1:
            print('Index:', index)
            input12 = int(input('Index select for removal?'))
            index.remove(input12)
            height.remove(input12)
            hip.remove(input12)
            sex.remove(input12)
            print('Total Index removed.')
            print(returning)
            return
        elif input11 ==2:
            print('Index: ', index)
            print('Height',  height)
            input13 = int(input('Index select?'))
            height.remove(input13)


            input14 = input('Enter height replacement: ')
            index.insert(input13)
            print(returning)
            return
            input13 = int(input('Index select?'))
        elif input11 ==3:
            print('Index:', index)
            print('Hip',      hip)
            input15 = int(input('which Hip entry would you like to remove?'))
        elif input11 ==4:
            print('index:',sex)
            print('sex: ', sex)

    elif input10 ==2:
        print(index)
        print(height)
        print(hip)
        print(sex)
        print(x)
    elif input10 == 3:
        return

    else:
        print(error)

    return
