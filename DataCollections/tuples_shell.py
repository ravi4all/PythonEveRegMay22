Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = 12
type(data)
<class 'int'>
data = 12,
type(data)
<class 'tuple'>
data = 2,3,5,2,2,4,5
type(data)
<class 'tuple'>
data = (2,3,5,2,2,4,5)
type(data)
<class 'tuple'>
data[0:4]
(2, 3, 5, 2)
data[4:0:-1]
(2, 2, 5, 3)
data[0] = 10
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data[0] = 10
TypeError: 'tuple' object does not support item assignment
del data[0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
data[0]
2
data[3]
2
data = "Ram", 40, "IT", 45000
data
('Ram', 40, 'IT', 45000)
name, age, dept, salary = data
name
'Ram'
age
40
dept
'IT'
salary
45000
salary += 5000
salary
50000
data
('Ram', 40, 'IT', 45000)
name, age, dept = data
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name, age, dept = data
ValueError: too many values to unpack (expected 3)
name, *details = data
name
'Ram'
details
[40, 'IT', 45000]
