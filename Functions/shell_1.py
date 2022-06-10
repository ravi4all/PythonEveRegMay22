Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def greet():
    msg = "Hello"
    def sayHello():
        print(msg,"Ravi")

        
greet()
def greet():
    msg = "Hello"
    def sayHello():
        print(msg,"Ravi")
    return msg

msg = greet()
print(msg)
Hello
def greet():
    msg = "Hello"
    def sayHello():
        print(msg,"Ravi")
    return sayHello

msg = greet()
msg()
Hello Ravi
lambda c : 9 / 5 * c + 32
<function <lambda> at 0x00000237D22E64D0>
(lambda c : 9 / 5 * c + 32)(34.77)
94.58600000000001
