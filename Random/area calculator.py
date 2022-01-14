s = 'Square'
r = 'Rectangle'
c = 'Circle'
t = 'Traingle'
s1 = 'Enter size required for',s,' here: '
r1 = 'Enter ',r,' height here:'
r2 = 'Enter ',r, 'width here: '
c1 = 'Enter',c, 'radius here'
t1 = 'Enter ',t,'side 1 here:'
t2 = 'Enter ',t,'side 2 here:'
x1 = 'the area is:'

s3 = float(0)
r5 = float(0)
c3 = float(0)
t5 = float(0)
t6 = float(0)
while True:
    shape = str(input('Enter shape required here (s, r, c, t): '))
    if (s == shape):
        s2 = float(input(s1))
        s3 = s2 * s2
        print (x1, s3)
        break
    if (r == shape):
        r3 = float(input(r1))
        r4 = float(input(r2))
        r5 = r3 * r4
        print (x1, r5)
        break
#i wasnt sure if i was allowed to inport libaries so i just went with the basic but its innacurate
    if (c == shape):
        c2 = float(input(c1))
        c3 = (3.142 * c2) *c2
        print (x1, c3)
        break
    if (t == shape):
        t3 = float(input(t1))
        t4 = float(input(t2))
        t3 = 0.5 * t3
        t4 = 0.5 * t4
        t5 = t3 * t4
        t6 = 2 * t5
        print (x1, t6)
        break


