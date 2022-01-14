#This program will calculate the appropriate PAYE based on the following:
#Employee personal allowance	£11,850 per year
#UK basic tax rate	 20% on annual earnings above the PAYE tax threshold and up to £34,500
#UK higher tax rate             40% on annual earnings from £34,501 to £150,000
#UK additional tax rate	                45% on annual earnings above £150,000
blo = 'you are below the tax bracket'
bhi = int(11850)
hilo = int(11851)
hihi = int(34500)
alo = int(34501)
sum = float()
annualsum= annual
while True:
    annual = float(input('Enter your annual income here required here (0-150,000+): '))
    if (bhi >= annual):
        print (blo)
        break
