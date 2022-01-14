w = 'wall'
wi1 = 'Enter ', w, ' width: '
hi1 = 'Enter ', w, 'height: '
w1 = float(0)
h1 = float(0)
w2 = float(0)
h2 = float(0)
width_walls = w1 * h1 * 2
length_walls = w2 * h2 * 2
walltot = (width_walls + length_walls)
x = int(0)
y = 'y'
n = 'n'
eco = 'eco'
stan = 'stan'
lux = 'lux'
under = 'undercoat for 0.5 extra? (y/n):'
price = float(0)

while True:
    shop = str(input('Enter paint shop? (y/n): '))
    if (y == shop):

        w1 = input(wi1)
        h1 = input(hi1)
        w2 = input(wi1)
        h2 = input(hi1)
        width_walls = w1 * h1 * 2
        length_walls = w2 * h2 * 2
        walltot = width_walls + length_walls

        print ('Width walls A&B are:',width_walls,'m2|','length walls C&D are:',length_walls,'m2| total:',walltot,'m2')

        paintsel = input('Enter which brand (eco,stan,lux):')
        if eco == paintsel:
            x = 1
            print(x)
        elif stan == paintsel:
            x = 2
            print(x)
        elif lux == paintsel:
            x = 3
            print(x)

    if 1 == x:
        undersel = input(under)
        if y == undersel:
            price = walltot * 0.95
            print ('Total m2 (AB+CD) is:',width_walls,'+',length_walls,'=',walltot)
            print ('paint (*0.95) =', price, '1-y')
            break
        else:
            price = walltot * 0.45
            print ('Total m2 (AB+CD) is:',width_walls,'+',length_walls,'=',walltot)
            print ('paint (*0.45) =', price, '1-n')
            break

    if 2 == x:
        undersel = input(under)
        if y == undersel:
            price = walltot * 1.50
            print ('Total m2 (AB+CD) is:',width_walls,'+',length_walls,'=',walltot)
            print ('paint (*1.50) =', price, '2-y')
            break
        else:
            price = walltot * 1.00
            print ('Total m2 (AB+CD) is:',width_walls,'+',length_walls,'=',walltot)
            print ('paint (*1.00) =', price, '2-n')
            break

    if 3 == x:
        undersel = input(under)
        if y == undersel:
            price = walltot * 2.25
            print ('Total m2 (AB+CD) is:',width_walls,'+',length_walls,'=',walltot)
            print('paint (*2.25) =', price, '3-y')
        else:
            price = walltot * 1.75
            print ('Total m2 (AB+CD) is:',width_walls,'+',length_walls,'=',walltot)
            print('paint (*1.75) =', price, '3-n')

    else: (n == shop)
    print('l8r m8r')
    break

# when using 'pound' with my software it gives an ascii error direct link to python (even inside of hash quotes)
# elif n== under breaks & else uses bottom
# when removing wall width, wall height & walltot from shop loop program breaks(ignores predetermined perameters within int loop)