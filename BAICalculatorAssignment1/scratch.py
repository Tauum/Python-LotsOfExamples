def main():
    set = []
    def userinput():
        counter = 0
        index = counter
        insex = str(input("M/F")).upper()
        if insex == 'M' or insex == 'F':
            sex = insex
        else:
            print('incorrect format, restart')
            userinput()

        inage = int(input('age 20-79'))
        if inage > 20 and inage <=80:
            age = inage
        else:
            print('incorrect format,restart')
            userinput()

        inheight = float(input('height in m [0.5]-[2.0]'))
        if inheight >= 0.5 and inheight <= 2:
            height = inheight
        else:
            print('incorrect format,restart')
            userinput()

        inhip = float(input('Hip in cm [30]-[150] > '))
        if inhip >= 30 and inhip <= 150 :
            hip = inhip
        else:
            print('incorect format, restart')
            userinput()

        def baifunc():
            a = height
            b = hip
            def baicalc(a, b):
                return (lambda a, b: (b / (a) ** 1.5) - 18)(a, b)
            bai = baicalc(a, b)
            bai = round(bai, 2)
            print('(Hip:',b,'/(Height)(**1.5):',a,'-18 =',bai)
            return bai

        BAI = baifunc()
        tempset = [index, sex, age, height, hip, BAI]
        print('\nlocal tempset',tempset)
        set.append(tempset)
        print('\nglobal set',set)
        retry = input('Reenter another data-set?').upper()
        if retry == 'y':
            userinput()
        elif retry =='n':
            def printglobal():
                print('global print test')
                print(set)
                return
            printglobal()
        return tempset

    userinput()
main()


#def num1(x):
  # def num2(y):
  #    return x * y
  # return num2
#res = num1(10)

#print(res(5))






