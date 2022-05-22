Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text = "Hello world, this is Python Programming"
text.lower()
'hello world, this is python programming'
text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
text.capitalize()
'Hello world, this is python programming'
text.swapcase()
'hELLO WORLD, THIS IS pYTHON pROGRAMMING'
text.title()
'Hello World, This Is Python Programming'
text.count('o')
4
text.count('i')
3
text.count('h')
2
text.index('i')
15
text.index('i',0)
15
text.index('i',16)
18
text.index('i',19)
36
text.find('i')
15
text.find('i',16)
18
text.find('i',19)
36
text.index('z')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.find('z')
-1
text.count('o')
4
count = text.count('o')
count
4
index = 0
for i in range(count):
    index = text.index('o', index)
    print(index, end=',')
    index += 1

    
4,7,25,30,
text.startswith('a')
False
text.startswith('H')
True
text.endswith('?')
False
text.endswith('.')
False
text.endswith('g')
True
text.isalpha()
False
text.isalnum()
False
text.isdigit()
False
text.islower()
False
text.isupper()
False
text.endswith('G')
False
text.split()
['Hello', 'world,', 'this', 'is', 'Python', 'Programming']
text.split(" ")
['Hello', 'world,', 'this', 'is', 'Python', 'Programming']
text.split(",")
['Hello world', ' this is Python Programming']
text.split("o")
['Hell', ' w', 'rld, this is Pyth', 'n Pr', 'gramming']
text = "    hello   "
text.strip()
'hello'
text.lstrip()
'hello   '
text.rstrip()
'    hello'
text.strip()
'hello'
text = "####hello$$$$"
text.strip()
'####hello$$$$'
text.strip('#')
'hello$$$$'
text = text.strip('#')
text
'hello$$$$'
text = text.strip('$')
text
'hello'
text.rfind('o')
4
text = "Hello world, this is Python Programming"
text.find('o')
4
text.rfind('o')
30
text.rindex('o')
30
text.replace('Hello', "Bye")
'Bye world, this is Python Programming'
text
'Hello world, this is Python Programming'
