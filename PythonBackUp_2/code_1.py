# This is first python programming
print("Welcome to Python Programming...")
a = 17
b = 3
c = a + b
d = a / b
print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {2} and {0} is {1}".format(b,c,a))
print("Div of {} and {} is {:.2f}".format(a,b,d))

#f-strings - format strings
print(f"Sum of {a} and {b} is {c}")
