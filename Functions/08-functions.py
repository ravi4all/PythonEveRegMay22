def calc(x,y):
    z = x + y
    print("Sum is",z)


print("""
1. Add
2. Sub
3. Div
4. Mul
""")

choice = int(input("Enter your choice : 1/2/3/4 : "))
fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

# operations = [add, sub, div, mul]
# operations[choice - 1](fnum, snum)
