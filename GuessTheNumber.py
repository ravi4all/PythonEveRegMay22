# Guess the number
import random

cpu = random.randint(1,100)
counter = 5
game = True
while game:
    guess = int(input("Enter your guess : "))
    if guess == cpu:
        print("Congrats you have guessed the number...")
        game = False
    elif guess > cpu:
        print("You have guessed a greater number...")
    elif guess < cpu:
        print("You have guessed a smaller number...")

    counter -= 1
    print("Chances Left ::",counter)
    if counter == 0:
        print("You Lose, Number was :",cpu)
        break
