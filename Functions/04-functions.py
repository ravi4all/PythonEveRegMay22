def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

choice = input("Enter your choice : 1/2/3/4 : ")
fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

if choice == "1":
    add(fnum, snum)
elif choice == "2":
    sub(fnum, snum)
elif choice == "3":
    div(fnum, snum)
elif choice == "4":
    mul(fnum, snum)
else:
    print("Invalid Choice...")
