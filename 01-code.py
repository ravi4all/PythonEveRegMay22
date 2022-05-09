a = 16
b = 7
c = a + b
d = a / b

print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {2} is {0}".format(c,a,b))

# f-strings - format strings
print(f"Sum of {a} and {b} is {c}")

print("Div of {} and {} is {:.4f}".format(a,b,d))

print(f"Div of {a} and {b} is {d:.3f}")




