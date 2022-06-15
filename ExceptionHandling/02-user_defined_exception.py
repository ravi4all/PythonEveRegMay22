def atm():
    pin = input("Enter your PIN : ")
    total = 10000
    if pin == "1234":
        print("Login Success...")
    else:
        # print("Login Failed...")
        raise ValueError("Login Failed...")

    amount = int(input("Enter amount you want to withdraw : "))
    total -= amount
    print("Remaining bal is",total)

chances = 3
print("You have 3 chances...")
try:
    atm()
except ValueError as msg:
    print(msg)
    chances -= 1
    print("Chances Left :",chances)
    try:
        atm()
    except ValueError as msg:
        print(msg)
        chances -= 1
        print("Chances Left :", chances)
        try:
            atm()
        except ValueError as msg:
            print(msg)
            chances -= 1
            print("Chances Left :", chances)
