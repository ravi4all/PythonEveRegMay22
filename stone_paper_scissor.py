#Stone Paper Scissor
import random

options = ["stone", "paper", "scissor"]
cpuScore = 0
userScore = 0
while True:
    user = input("Enter your choice : stone / paper / scissor : ")
    cpu = random.choice(options)
    print("User : {}, CPU : {}".format(user, cpu))
    if user == cpu:
        print("Tie...")
    elif user == "stone" and cpu == "paper":
        print("CPU Win...")
        cpuScore += 1
    elif user == "paper" and cpu == "scissor":
        print("CPU Win...")
        cpuScore += 1
    elif user == "scissor" and cpu == "stone":
        print("CPU Win...")
        cpuScore += 1
    elif user == "stone" and cpu == "scissor":
        print("User Win...")
        userScore += 1
    elif user == "paper" and cpu == "stone":
        print("User Win...")
        userScore += 1
    elif user == "scissor" and cpu == "paper":
        print("User Win...")
        userScore += 1
    print("CPU Score : {}, User Score : {}".format(cpuScore, userScore))
