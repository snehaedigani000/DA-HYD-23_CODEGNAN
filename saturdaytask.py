'''#Question 1: Student Marks Manager
#Task: Write a program that accepts marks, adds more values, removes 

selected values, and displays the final list.
marks = []
for i in range(3):
    m = int(input("Mark: "))
    marks.append(m)
print("Marks:", marks)
marks.insert(0, 90)
marks.extend([75, 85])
print("Updated:", marks)
if 75 in marks:
    marks.remove(75)
    print("75 removed")
x = marks.pop()
print("Removed:", x)
print("Final:", marks)
print("Count:", len(marks))
'''

'''#Question 2: Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]
numbers.sort()
print("Asc:", numbers)
numbers.reverse()
print("Desc:", numbers)
n = int(input("Search: "))
if n in numbers:
    print("Found")
    print("Count:", numbers.count(n))
    print("Index:", numbers.index(n))
else:
    print("Not found")
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
'''
'''
#Question 3: Even and Odd Number Separator
numbers=[10,15,20,25,30,35]
even=[]
odd=[]
for i in numbers:
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("odd numbers:",odd)
print("first three numbers:",numbers[:3])
print("last three numbers:",numbers[-3:])
backup=numbers.copy()
print("backup list:",backup)
numbers.clear()
print("final list:",numbers)
'''
'''
#Question 4: Unique Name Manager
names=["Asha","Rahul","Asha","John","Rahul"]
names=set(names)
print("Names:",names)
names.add("Meera")
names.update(["Arun","Priya"])
if "John" in names:
    names.remove("John")
names.discard("David")
for n in names:
    print(n)
'''
'''
#Question 5:Course Student Comparison 

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}
both_courses = python_students.union(da_students)

common_students = python_students.intersection(da_students)

only_python = python_students.difference(da_students)

only_one_course = python_students.symmetric_difference(da_students)

is_subset = da_students.issubset(python_students)

is_superset = python_students.issuperset(da_students)

is_disjoint = python_students.isdisjoint(da_students)

print("Students from both courses:")
for student in both_courses:
    print(student)
print("\nStudents learning both courses:")
for student in common_students:
    print(student)
print("\nStudents learning only Python:")
for student in only_python:
    print(student)
print("\nStudents learning only one course:")
for student in only_one_course:
    print(student)
print("\nRelationship Results:")
if is_subset:
    print("DA set is a subset of Python set: True")
else:
    print("DA set is a subset of Python set: False")
if is_superset:
    print("Python set is a superset of DA set: True")
else:
    print("Python set is a superset of DA set: False")
if is_disjoint:
    print("Both sets are disjoint: True")
else:
    print("Both sets are disjoint: False")
'''










