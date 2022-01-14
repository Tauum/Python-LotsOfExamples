while True:
    print ('please input which you would like to conver(m/k)')
    sel = input()
    if  'm' == sel:
        miles = float(input('input distance:'))
        kilometer = (miles * 1.609344)
        print(kilometer, 'kilometers')
        
    else:
        kilometer = float(input('input distance:'))
        miles = (kilometer / 1.609344)
        print(miles, 'miles')      
