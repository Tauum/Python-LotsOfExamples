#info = [[index],[sex],[age],[height],[hip],[bai][healhiness]]
set = [[    0,    'm',   20,    190,    90,   20, 'Heahtly'],
       ['m','m','m'],
       [7,8,9],
       [10,11,12],
       [13,14,15],
       [16,17,18],
       [19,20,21]]

tempset = [[],#index
           []]#sex

def sexInput():
    counter = 0
    x = input('input sex').upper()
    if x == 'M' or x == 'F':
        y = counter
        z = 2
        counter +=1
        tempset[z].insert(y,x)
        print('Sex:',tempset[2])
        return sexInput()
    elif x == 'TRIGGERED':
        set[1].insert(-1,tempset)
        print('Tempset total:',tempset)
        exit()
    else:
        print('there are only two genders')
        return sexInput()

#sexInput()


#set = [['x','y']]
#tempset = []
#print(set[0][1])

#x = 0
#x = int(input(' array select:'))
#y = int(input('index select:'))
#z = int(input('element input:'))
#tempset[x].insert(y,z)
#print(tempset)

#def amendMenu():
  #  print('index:',tempset[0])
 #   print('sex:',tempset[1])
 #   print('age:',tempset[2])
 #   print('height:',tempset[3])
  #  print('hip:',tempset[4])
  #  print('BAI:',tempset[5])
  #  print('Healthiness:',tempset[6])

#amendMenu()

#tempset = [index[# ],
# sex[],
# age[],
# height[],
# hip[],
# bai[],
# healthiness[]]

#x = int(input('input val:'))
#y = int(input('input index:'))
#z = int(input('input array:'))

#tempset[z].insert(y,x)
#print(tempset)

