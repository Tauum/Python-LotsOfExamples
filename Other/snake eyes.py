import random
game_start = input("Would you like to roll the dice?")

(die1) = int(0)
(die2) = int(0)
dieadd = int(die1) + int(die2)

def dice_roll():
    die1 = int(random.randint(1,6))
    die2 =  int(random.randint(1, 6))
    print (die1)
    print (die2)
    print (dieadd)

if dieadd == 2:
    print ("Congratulations")

elif dieadd != 2:
    print ("sorry not this time!")
    global play_again
    dice_roll()


if game_start == "yes" or "y":
    dice_roll()
    while play_again == "yes" or 'Y':
        dice_roll()
elif game_start == "no" or 'n':
    print("Game Over")
else:
    print("Input not recognized")