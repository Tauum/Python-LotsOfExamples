blop = 'Ienligable the tax bracket'
bhip = 'Eligable for 20% tax'
hihip = 'Eligable for 40% tax'
addhip = 'Eligable for 45% tax'
bhi = int(11850)
hihi = int(34501)
addhi = int(150000)
sum1 = float(0)
annual = float(0)
aftertax = float(0)
annualsum = annual


while True:
    annual = float(input('Enter your annual income here required here (0-150,000+): '))
    if (bhi >= annual):
        print (blop)
        break
    elif (bhi <= annual):
        annualsum
        print (bhip)
        annualsum = annual / 100 * 20
        aftertax = annualsum - annual
        print ('annual: ',annual,' -', '20% tax ', annualsum,'=', aftertax,' After tax')
    elif (hihi <= annual):
        print (hihip)
        annualsum = annual / 100 * 40
        aftertax = annualsum - annual
        print ('annual: ',annual,' -', '40% tax ', annualsum,'=', aftertax,' After tax')
    elif (addhi <= annual):
        print (addhip)
        annualsum = annual / 100 * 45
        aftertax = annualsum - annual
        print ('annual: ',annual,' -', '45% tax ', annualsum,'=', aftertax,' After tax')

#prints correct vaulues but does not print tax % right for some reason
