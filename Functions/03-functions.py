def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def calc():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    add(x,y)
    sub(x,y)

calc()