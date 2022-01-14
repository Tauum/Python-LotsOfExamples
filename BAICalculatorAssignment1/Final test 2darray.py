                                                                                        #globals


def main():
    # input/error handling
    error = 'Error, Incorrect (format/value)'
    returned = 'Returned.'
    entryRem = 'Input entry removed.'
    na = 'N/A'
    # data storage
    border = ' -' * 48
    dataset = []
    counter = int()
    x = 0
    sexres = str()
    ageres = int()
    def userinput(x,counter,sexres,ageres):
        print(x, sexres, ageres)
        tempset = [counter,sexres,ageres]
        tempset.append(counter)
        sexInput()
        ageInput()
        x = len(dataset)
        dataset.append(tempset)
        counter+=1
        x +=1
        print(tempset)
        print(dataset)
        return

    def sexInput():  # user inputs sex
        print('\n\t', border, '\n')
        inSex = input("\t--\tSex - [M/F] > ").upper()
        if inSex == 'M' or inSex == 'F':
            sexres = inSex
            #tempset.insert(choice,sexres)
            return sexres
        else:
            print('\t\t', entryRem, error)
            return sexInput()

    def ageInput():  # user inputs age
        inAge = input("\t--\tAge - [20]-[79] > ")
        try:
            inAge = int(inAge)
            res = isinstance(inAge, int)
            if res == True:
                if inAge >= 20 and inAge <= 79:
                    ageres = inAge
                    #tempset.insert(choice,ageres)
                    return ageres
                else:
                    print('\t\t', entryRem, error)
                    return ageInput()
        except ValueError:
            print('\t\t', entryRem, error)
            return ageInput()



    print('\n\t', border, '\n')
    menustr = ['---------[ Menu ]---------', '[1 - Input data         ]', '[2 - View input data    ]',
               '[3 - Amend data         ]', '[4 - View set results   ]', '[5 - BAI chart          ]'
        , '[6 - Restart            ]', '[7 - Exit               ]']
    for i in range(len(menustr)):
        print('\t\t\t''{:<50s}'.format(menustr[i]))
    input1 = input('\n\t\t--\tInput > ')
    if input1 == '1':  # input menu
        userinput(x,counter,sexres,ageres)
    elif input1 == '2':
        print('2')
        exit()
    else:
        print(error)
        main()

main()