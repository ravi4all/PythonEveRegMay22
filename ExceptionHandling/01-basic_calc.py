try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = a + b
    d = a - b
    e = a / b
    f = a * b

except ZeroDivisionError:
    print("Cannot divide by zero...")

except ValueError:
    print("Invalid Input...Please enter a valid number...")

# Always write BaseException at the end
except BaseException:
    print("Some unexpected error...")

else:
    print("Sum is", c)
    print("Sub is", d)
    print("Div is", e)
    print("Mul is", f)

finally:
    # Always use finally to close files and connections
    print("I will always execute...")
