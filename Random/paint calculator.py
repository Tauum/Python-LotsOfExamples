w = 'wall'
wi1 = 'Enter ',w,' width here: '
hi1 = 'Enter ',w, 'height here: '
x = int(0)
y = 'y'
n = 'n'
eco = 'eco'
stan = 'stan'
lux = 'lux'
under = 'undercoat for £0.5 extra? (y or n):'

while True:
    shop = str(input('Enter paint shop here (y or n): '))
    if (y == shop):
        w1 = float(input(wi1))
        h1 = float(input(hi1))
        w2 = float(input(wi1))
        h2 = float(input(hi1))

        width_walls = w1 * h1
        length_walls = w2 * h2
        walltot = width_walls + length_walls
        print ('Width walls A&B are: ', width_walls,'m2|',' length walls C&D are: ',length_walls,'m2|' )

        paintsel = str(input('Enter which brand (eco,stan,lux): '))
        if (eco == paintsel):
            x = 1
            print(x)
        elif (stan == paintsel):
            x = 2
            print(x)
        elif (lux == paintsel):
            x = 3
            print(x)
            
    while (1 == x):
        undersel = (input(under))
        if (y == under):
            walltot = walltot * 95
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: £', walltot)
        elif (n == under):
            walltot = walltot * 45
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: £', walltot)
            
    while (2 == x):
        undersel = str(input(under))
        if (y == under):
            walltot = walltot * 150
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: £', walltot)
        elif (n == under):
            walltot = walltot * 100
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: £', walltot)
            
    while (3 == x):
        undersel = str(input(under))
        if (y == under):
            walltot = walltot * 225
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: £', walltot)
        elif (n == under):
            walltot = walltot * 175
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: £', walltot)

    if (n == shop):
        print('l8r looser')
        break
