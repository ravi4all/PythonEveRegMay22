def wrapper():
    # Local variables for wrapper function
    x = 10
    y = 12
    def add():
        # Global variable for add function
        z = x + y
        print("Sum is",z)

    def sub():
        # Global variable for sub function
        z = x - y
        print("Sub is",z)

    # we can call add and sub only inside wrapper function
    # add()
    # sub()

wrapper()
