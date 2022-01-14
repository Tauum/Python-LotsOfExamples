w = 'wall'
wi1 = 'Enter ',w,' width here: '
hi1 = 'Enter ',w, 'height here: '
x = int(0)
y = 'y'
n = 'n'
eco = 'eco'
stan = 'stan'
lux = 'lux'
under = 'undercoat for 0.5 extra? (y or n):'
wallt = ()
wall2 = ()
width_walls = ()
length_walls = ()

while True:
    shop = str(input('Enter paint shop here (y or n): '))
    if y == shop:
        w1 = float(input(wi1))
        h1 = float(input(hi1))
        w2 = float(input(wi1))
        h2 = float(input(hi1))

        print ('Width walls A&B are: ', width_walls,'m2',' length walls C&D are: ',length_walls,'m2' )
        wallt = width_walls + length_walls
        paint_sel = str(input('Enter which brand (eco,stan,lux): '))
        if eco == paint_sel:
            x = 1
            print(x)
        if stan == paint_sel:
            x = 2
            print(x)
        if lux == paint_sel:
            x = 3
            print(x)
    while 1 == x:
        under_sel = str(input(under))
        if y == under:
            wallt2 = wallt * 95
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: ', wallt)
        elif n == under:
            wallt2 = wallt* 45
            print ('Total m2 is: ', width_walls, '*', length_walls, 'for: ', wallt)
    while 2 == x:
        under_sel = str(input(under))
        if y == under:
            wallt2 = wallt * 150
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: ', wallt)
        elif n == under:
            wallt2 = wallt * 100
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: ', wallt)
    while 3 == x:
        under_sel = str(input(under))
        if y == under:
            wallt2 = wallt * 225
            print ('Total m2 is: ',width_walls, '*', length_walls,'for: ', wallt)
        elif n == under:
            wallt2 = wallt * 175
            print ('Total m2 is: ', width_walls, '*', length_walls, 'for: ', wallt)
        break
    if n == shop:
        print('l8r looser')
