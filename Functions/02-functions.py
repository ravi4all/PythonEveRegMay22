# Scope of variables:
# - Global Scope
# - Local Scope

# Global Variables - variables defined outside the function
x = 12
y = 20

def add():
    # Local Variables - accessible only inside function
    z1 = x + y
    print("Sum is",z1)

def sub():
    z2 = x - y
    print("Sub is",z2)

add()
sub()

# print(z1, z2)
