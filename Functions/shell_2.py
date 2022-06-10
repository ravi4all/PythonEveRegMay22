Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def greet():
    print("Hello")
    yield "How are you ?"
    print("I am good...")
    yield "Ok Bye"

    
int x = 10
SyntaxError: invalid syntax
x = 10
x()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x()
TypeError: 'int' object is not callable

x = [3,2,4]
x()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x()
TypeError: 'list' object is not callable
def greet():
    print("Hello")
    yield "How are you ?"
    print("I am good...")
    yield "Ok Bye"

    












def sayHello():
    print("Hello User")

    
sayHello()
Hello User
msg = sayHello()
Hello User
print(msg)
None
def sayHello():
    return "Hello User"

msg = sayHello()
print(msg)
Hello User
def greet():
    print("Hello")
    yield "How are you ?"
    print("I am good...")
    yield "Ok Bye"

    
greet()
<generator object greet at 0x000001BA5DD65770>
msg = greet()
next(msg)
Hello
'How are you ?'
userMsg = next(msg)
I am good...
userMsg
'Ok Bye'
def greet():
    print("Hello")
    return "How are you ?"
    print("I am good...")
    return "Ok Bye"

msg = greet()
Hello
msg
'How are you ?'
def views():
    view = 0
    while True:
        view += 1
        yield view

        
obj = views()
next(obj)
1
next(obj)
2
next(obj)
3
next(obj)
4
