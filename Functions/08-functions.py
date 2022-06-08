def calc(x,y,opr):
    expression = x + opr + y
    print(expression)


print("""
1. Add
2. Sub
3. Div
4. Mul
""")

choice = int(input("Enter your choice : 1/2/3/4 : "))
fnum = input("Enter first number : ")
snum = input("Enter second number : ")

operations = {
    1 : "+",
    2 : "-",
    3 : "/",
    4 : "*"
}
opr = operations.get(choice)
calc(fnum, snum, opr)
