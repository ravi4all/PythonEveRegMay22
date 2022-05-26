Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = {"name" : "Ram", "age" : 40, "salary" : 45000, "dept" : "IT"}
type(data)
<class 'dict'>
data[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data[0]
KeyError: 0
data["name"]
'Ram'
data["age"]
40
data["salary"]
45000
data["dept"]
'IT'
data = {"name" : "Ram", "age" : 40, "salary" : 45000, "dept" : "IT", "name" : "Raman"}
data
{'name': 'Raman', 'age': 40, 'salary': 45000, 'dept': 'IT'}
data["name"] = "Ram"
data
{'name': 'Ram', 'age': 40, 'salary': 45000, 'dept': 'IT'}
data["address"] = "Delhi"
data
{'name': 'Ram', 'age': 40, 'salary': 45000, 'dept': 'IT', 'address': 'Delhi'}
data.keys()
dict_keys(['name', 'age', 'salary', 'dept', 'address'])
data.values()
dict_values(['Ram', 40, 45000, 'IT', 'Delhi'])
data.items()
dict_items([('name', 'Ram'), ('age', 40), ('salary', 45000), ('dept', 'IT'), ('address', 'Delhi')])
data.get('name')
'Ram'
data['name']
'Ram'
data['email']
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    data['email']
KeyError: 'email'
data.get('email')
data.get('email', "Not Available")
'Not Available'
data.get('name', "Not Available")
'Ram'
data.popitem()
('address', 'Delhi')
data
{'name': 'Ram', 'age': 40, 'salary': 45000, 'dept': 'IT'}
data.pop('age')
40
data
{'name': 'Ram', 'salary': 45000, 'dept': 'IT'}
data.update({"email" : "ram12@gmail.com", "age" : 40})
data
{'name': 'Ram', 'salary': 45000, 'dept': 'IT', 'email': 'ram12@gmail.com', 'age': 40}
for item in data:
    print(item)

    
name
salary
dept
email
age
for item in data:
    print(item, "::", data[item])

    
name :: Ram
salary :: 45000
dept :: IT
email :: ram12@gmail.com
age :: 40
for key in data:
    print(key, "::", data[key])

    
name :: Ram
salary :: 45000
dept :: IT
email :: ram12@gmail.com
age :: 40
for key in data:
    print(key, "::", data.get(key))

    
name :: Ram
salary :: 45000
dept :: IT
email :: ram12@gmail.com
age :: 40
names = ["John", "Shawn", "Mac", "Sam", "Tom"]
dept = ["IT", "Admin", "Sales", "IT", "Sales"]
sal = [45000, 56000, 65000, 40000, 70000]
data = {"names" : names, "dept" : dept, "salary" : sal}
data
{'names': ['John', 'Shawn', 'Mac', 'Sam', 'Tom'], 'dept': ['IT', 'Admin', 'Sales', 'IT', 'Sales'], 'salary': [45000, 56000, 65000, 40000, 70000]}
data["names"]
['John', 'Shawn', 'Mac', 'Sam', 'Tom']
data["dept"]
['IT', 'Admin', 'Sales', 'IT', 'Sales']
data["sal"]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data["sal"]
KeyError: 'sal'
data["salary"]
[45000, 56000, 65000, 40000, 70000]
data["names"][0]
'John'
data["names"][3]
'Sam'
data["dept"][0]
'IT'
data["dept"][3]
'IT'
for i in range(len(data["names"])):
    print(data["names"][i], data["dept"][i], data["salary"][i])

    
John IT 45000
Shawn Admin 56000
Mac Sales 65000
Sam IT 40000
Tom Sales 70000
