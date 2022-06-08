import calculator

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

choice = int(input("Enter your choice : 1/2/3/4 : "))
fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

operations = {
    1 : calculator.add,
    2 : calculator.sub,
    3 : calculator.div,
    4 : calculator.mul
}
result = operations.get(choice)(fnum, snum)
print("Result is :",result)