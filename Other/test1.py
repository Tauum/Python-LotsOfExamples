import random


def guess(x):
    random_number = random.randint(1, x)
    print(random_number)
    guess = 0
    while guess != random_number:
        print("Number range: 1 - 10")
        guess = int(input("Guess a number: "))
        print(guess)
        if guess > random_number:
            print("Incorrect! Number too high.\n")
        elif guess < random_number:
            print("Incorrect! Number too high.\n")
        if guess == random_number:
            print(f"Correct! The number was {random_number}")

guess(10)