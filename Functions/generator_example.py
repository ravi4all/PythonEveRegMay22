Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def counter():
    x = 0
    return x
    print("Hello")

    
counter()
0
def counter():
    x = 0
    while True:
        x += 1
        return x

    
counter()
1
counter()
1
x = 0
def counter():
    while True:
        x += 1
        return x

    
counter()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    counter()
  File "<pyshell#16>", line 3, in counter
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
def counter():
    x = 0
    while True:
        x += 1
        return x

    
def counter():
    x = 0
    while True:
        x += 1
        return x

    
counter()
1
counter()
1
counter()
1
def counter():
    x = 0
    while True:
        x += 1
        yield x

        
counter()
<generator object counter at 0x000001926AFB5770>
count = counter()
next(count)
1
next(count)
2
next(count)
3
next(count)
4
for i in range(6):
    print(next(count))

    
5
6
7
8
9
10
def greet():
    print("Hello")
    yield "Bye"
    print("Take Care")
    print("Ok...")

    
greet()
<generator object greet at 0x000001926AFB5770>
msg = greet()
next(msg)
Hello
'Bye'
next(msg)
Take Care
Ok...
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    next(msg)
StopIteration
