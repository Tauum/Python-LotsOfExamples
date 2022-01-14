marbleCost = 12
money = int(100)
counter = 0

while money >= 12:
    money=money-marbleCost
    counter += 1
    print(str(counter) + " marbles owned")
    print("money: £" + str(money))

    if money <=12:
      print("insufficient funds")
      print(str(counter) + " total marbles owned")