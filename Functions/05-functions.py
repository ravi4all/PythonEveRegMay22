# Positional/Required Arguments
# def greet(firstname, lastname):
#     print("Hello",firstname, lastname)

# greet()
# greet("Ravi")
# greet("Ram", "Sharma")

# Default arguments
def greet(firstname, lastname="", address="Delhi"):
    print("Welcome to",address)
    print("Hello",firstname, lastname)

# Keyword arguments
# greet(firstname="Ram", lastname="Sharma")
# greet(lastname="sharma", firstname="Ram")

greet("Ram")
greet("Ram", "Sharma")
greet("Ram", "Sharma", "Chennai")