Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = []
data.append(12)
data
[12]
data.append(10)
data
[12, 10]
data.append(23)
data.append(100)
data.append(50)
data.append("Ram")
data
[12, 10, 23, 100, 50, 'Ram']
type(data)
<class 'list'>
type(data[0])
<class 'int'>
type(data[-1])
<class 'str'>
data.pop()
'Ram'
data
[12, 10, 23, 100, 50]
data.pop(3)
100
data
[12, 10, 23, 50]
data.insert(3,200)
data
[12, 10, 23, 200, 50]
data.remove(10)
data
[12, 23, 200, 50]
data.index(200)
2
data[2] = 100
data
[12, 23, 100, 50]
data.append(12,4,3,2,2,2,1,124)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data.append(12,4,3,2,2,2,1,124)
TypeError: list.append() takes exactly one argument (8 given)
data.append([12,4,3,2,2,2,1,124])
data
[12, 23, 100, 50, [12, 4, 3, 2, 2, 2, 1, 124]]
data.pop()
[12, 4, 3, 2, 2, 2, 1, 124]
data
[12, 23, 100, 50]
data.extend([12,4,3,2,2,2,1,124])
data
[12, 23, 100, 50, 12, 4, 3, 2, 2, 2, 1, 124]
data.count(2)
3
data.count(12)
2
data.extend(10)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    data.extend(10)
TypeError: 'int' object is not iterable
data.sort()
data
[1, 2, 2, 2, 3, 4, 12, 12, 23, 50, 100, 124]
data.sort(reverse=True)
data
[124, 100, 50, 23, 12, 12, 4, 3, 2, 2, 2, 1]
data = [["Ram",30,50000],["Shyam",40,80000],["John",35,60000]]
data
[['Ram', 30, 50000], ['Shyam', 40, 80000], ['John', 35, 60000]]
data[0]
['Ram', 30, 50000]
data[1]
['Shyam', 40, 80000]
data[2]
['John', 35, 60000]
data[0][0]
'Ram'
data[0][1]
30
data[0][2]
50000
data[1][0]
'Shyam'
data = [["Ram", "Shyam", "John"],["IT","HR","IT"],[45000,56000,65000]]
emp = ['John', 35, 60000]
for i in range(len(emp)):
    print(emp[i])

    
John
35
60000
for i in range(len(emp)):
    print(i, "::", emp[i])

    
0 :: John
1 :: 35
2 :: 60000
len(emp)
3
for item in emp:
    print(item)

    
John
35
60000
data = [["Ram", "Shyam", "John"],["IT","HR","IT"],[45000,56000,65000]]
for i in range(len(data[0])):
    print(data[0][i], data[1][i], data[2][i])

    
Ram IT 45000
Shyam HR 56000
John IT 65000
for i in range(len(data[0])):
    for j in range(len(data[i])):
        print(data[j][i], end=',')
    print()

    
Ram,IT,45000,
Shyam,HR,56000,
John,IT,65000,
for i in range(len(data[0])):
    for j in range(len(data[i])):
        print(data[i][j], end=',')
    print()

    
Ram,Shyam,John,
IT,HR,IT,
45000,56000,65000,
