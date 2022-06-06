# *args - variable length arguments / arbitrary arguments
def add(*x):
    # print(x)
    sum = 0
    for i in x:
        sum += i
    print("Sum is",sum)

add()
add(3)
add(3,4)
add(4,3,4)
add(4,3,4,56,6,4)

# **kwargs - Keyword Variable Length Arguments
def person(**details):
    print(details)

person(name="Ram", dept="IT")
person(name="Shyam")
person(id=101, name="Mohit", salary=45000, dept="IT")