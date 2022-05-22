Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "Hello world, This is Python Programming..."
text = 'Hello world, This is Python Programming...'
text = """Hello world,
This is Python Programming..."""
print(text)
Hello world,
This is Python Programming...
text = "Hello Python"
print(text)
Hello Python
text = "Hello "Python""
SyntaxError: invalid syntax
text = "Hello \"Python\""
print(text)
Hello "Python"
text = "Hello \n Python"
print(text)
Hello 
 Python
text = "Hello \\n Python"
print(text)
Hello \n Python
text = 'Hello "Python"'
print(text)
Hello "Python"
text = "Hello world, This is Python Programming..."
len(text)
42
import sys
sys.getsizeof('')
49
sys.getsizeof('h')
50
sys.getsizeof('he')
51
sys.getsizeof('hel')
52
sys.getsizeof('hell')
53
sys.getsizeof(12)
28
text = "Hello world, This is Python Programming..."
len(text)
42
text[0]
'H'
text[10]
'd'
text[20]
' '
text[40]
'.'
text[0:4]
'Hell'
text[10:14]
'd, T'
text[10:24]
'd, This is Pyt'
text[10:]
'd, This is Python Programming...'
text[:12]
'Hello world,'
text[:]
'Hello world, This is Python Programming...'
text[0:30:2]
'Hlowrd hsi yhnP'
text[0:30:3]
'Hlwl iiPh '
text[10:0]
''
text[10:0:-1]
'dlrow olle'
text[10::-1]
'dlrow olleH'
text[-5]
'n'
text[1:5]
'ello'
text[-1:-5]
''
text[-1:-5:-1]
'...g'
text
'Hello world, This is Python Programming...'
text[::-1]
'...gnimmargorP nohtyP si sihT ,dlrow olleH'
