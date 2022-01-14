# Output message explaining purpose of program
print("This program will do the hard work for you and calculate the total cost of painting a room rectangular room, using dimensions values you are providing.")
# Ask user to input dimension values
print("Enter the numeric value of Lenght:")
length=float(input())
print("Enter the numeric value of Width:")
width=float(input())
print("Enter the numeric value of Height:")
height=float(input())
# Store room area in a variable
areaRoom=2*(width*length+height*length+height*width)
# Ask user to choose one of the painting options in a list
print("Please select one of the options below by entering its coresponding number:")
print("1. Economy - £0.45 per m2\n2. Standard - £1.00 per m2\n3. Luxury - £1.75 per m2")
# Accept value and store it in a variable
package= int(input())
# If option 1 is selected, calculate the total cost.
if package =="1":
    totalCost= areaRoom*0.45
# If option 2 is selected, calculate the total cost.
elif package =="2":
    totalCost= areaRoom*1
# If option 3 is selected, calculate the total cost.
else:
    totalCost=areaRoom*1.75
# Output message showing total cost with 2 decimals, in GBP
print("The total cost for painting this room is £{:0.2f}".format(totalCost))
# Ask user for optional service, provide 2 options
print("Would you like to optionally undercoat at £0.50/m2?")
print("Choose an option: \n1. Yes\n2. No")
# Accept and store value into a variable
optional=input()
# If value is 1, calculate painting + undercoating cost
if optional =="1":
    lastCost= totalCost+(areaRoom*0.50)
    # Output message with detailed bill
    print("Thank you for choosing us! Your bill below:")
    print("Room Surface Area:", areaRoom,"m2", "\nPainting Cost: £{:0.2f}".format(totalCost), "\nPainting + Undercoating: £{:0.2f}".format(lastCost))
# If value is not 1, output goodbye message
else:
    print("See you next time!")
    




