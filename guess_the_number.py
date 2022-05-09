import random

cpu = random.randint(1,100)
counter = 5
game = True
while game:
    guess = int(input("Guess the number : "))
    if guess == cpu:
        print("Congrats, You have guessed the number...")
        game = False
        break
    elif guess > cpu:
        print("You have guessed a larger number")
    elif guess < cpu:
        print("You have guessed a smaller number")
    counter -= 1
    print("Chances Left ::",counter)
    if counter == 0:
        print("You Lose...Number was",cpu)
        game = False
        break
