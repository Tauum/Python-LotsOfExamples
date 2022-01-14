noBai=[5,4,2,1,6,7,8,2,10]

def modeof(listObject):
    n= len(listObject) # 5
    occulist1=[]
    values1=[]
    mode=[]
    occurence=[]
    if n>1:
        for i in range(n):
            print(i)
            occuNo = listObject.count(listObject[i])
            if occuNo >1:
                occulist1.append(occuNo)
                print(occulist1)
                values1.append(listObject[i])
                print(values1)
            if occuNo == max(occulist1):
                    occurence.append(occuNo)
                    mode.append(listObject[i])
            mode = set(mode)
            occurence = set(occurence)

            if len(mode) < 1 and len(occurence) < 1:
                print("Error. List is probably empty or there are only unique values.")
            else:
                return mode, occurence
        mode, occurence = modeof(noBai)
        print("The mode of the list is", mode, "\n", "with an occurence rate of ", occurence)
#modeof(noBai)

median=sorted(noBai)[len(noBai)//2]
print (median)
median=[len(noBai)//2]
print (median)
print(sorted(noBai))