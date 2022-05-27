data = {"names" : ["John", "Shawn", "Mac", "Sam", "Tom"],
        "dept" : ["IT", "Admin", "Sales", "IT", "Sales"],
        "salary" : [45000, 56000, 65000, 40000, 70000]}

'''
1. Take emp name as input from user and print his dept and salary
without using any loop
2. Print average salary of IT Department
3. Print all employees who belongs to sales department
4. Print all employees whose name start with 'S'
5. Print those employees whose salary is greater than 50000
6. Increment salary of all employees by 5000
'''

emp_name = input("Enter Emp Name : ")
emp_name = emp_name.capitalize()
emp_index = data["names"].index(emp_name)
emp_dept = data["dept"][emp_index]
emp_sal = data["salary"][emp_index]
print("Emp Name : {}, Emp Dept : {}, Emp Salary : {}".format(emp_name,
                                                             emp_dept,
                                                             emp_sal))

print("*" * 50)

totalSalary = 0
for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        totalSalary += data["salary"][i]
count = data["dept"].count("IT")
avg = totalSalary / count
print("Average Salary of IT :",avg)

print("*" * 50)

for i in range(len(data["names"])):
    if data["dept"][i] == "Sales":
        print(data["names"][i], data["dept"][i])

print("*" * 50)

print("Salary Before Increment...")
for i in range(len(data["names"])):
    print("Name : {}, Salary : {}".format(data["names"][i], data["salary"][i]))

for i in range(len(data["names"])):
    data["salary"][i] += 5000

print("Salary After Increment...")
for i in range(len(data["names"])):
    print("Name : {}, Salary : {}".format(data["names"][i], data["salary"][i]))

