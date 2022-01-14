
def heightInput(height, hcm):
    input2 = input('Height? (y/n): ').upper()
    if input2 == 'Y':
        heightCalc(hcm)
        height.append(hcm)
        return
    elif input2 == 'N':
        height.append(nax)
        print(returning)
        return
    else:
        print(error)
        heightInput(height)
    return


def heightCalc(hcm):
    input21 = input('M,ft,in? (1,2,3)')
    if input21 == '1':
        hc = float(input('M (0-3): '))
        if hc > 0 and hc < 3:
            hcm = hc * 10
            return hcm
        else:
            print(error, 'entry removed')
            heightInput(height)
    elif input21 == '2':
        hc = float(input('ft (0-8): '))
        if hc > 0 and hc < 8:
            hcft = hc * 3.2808398950131
            height.append(hcft)
            print(returning)
            return
        else:
            print(error, 'entry removed')
            heightInput(height)

    elif input21 == '3':
        hc = float(input('inches (0-150): '))
        if hc > 0 and hc < 150:
            hcin = hc * 2.54
            height.append(hcin)
            return
        else:
            print(error, 'entry removed')
            heightInput(height)
    else:
        print(error)
        heightInput(height)


def hipInput(hip, hmm):
    input3 = input('Hip circumference? (y/n): ').upper()
    if input3 == 'Y':
        hipCalc(hmm)
        hip.append(hmm)
        return
    elif input3 == 'N':
        hip.append(nax)
        print(returning)
        return
    else:
        print(error)
        hipInput(hip)
    return


def hipCalc(hmm):
    input31 = input('M,ft,in? (1,2,3)')
    if input31 == '1':
        hm = float(input('M (0-2): '))
        if hm > 0 and hm < 2:
            hmm = hm * 10
            hip.append(hmm)
            return
        else:
            print(error, 'entry removed')
            hipInput(hip)

    elif input31 == '2':
        hm = float(input('ft (0-6): '))
        if hm > 0 and hm < 6:
            hmft = hm * 3.2808398950131
            hip.append(hmft)
            return
        else:
            print(error, 'entry removed')
            hipInput(hip)

    elif input31 == '3':
        hm = float(input('inches (0-100): '))
        if hm > 0 and hm < 100:
            hmi = hm * 2.54
            hip.append(hmi)
            return
        else:
            print(error, 'entry removed')
            hipInput(hip)
    else:
        print(error)
        hipInput(hip)


def ageInput(age):
    input5 = input('Input age? (y/n): ').upper()
    if input5 == 'Y':
        agein = int(input('Age (20-79): '))
        if agein >= 20 and agein <= 79:
           age.append(agein)
           print(returning)
           return
        else:
            print(error, 'entry removed')
            ageInput(age)
            return
    elif input5=='N':
        age.append(nax)
        print(returning)
        return
    else:
        print(error)
        ageInput(age)
    return
