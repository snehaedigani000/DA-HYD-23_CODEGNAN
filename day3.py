'''
#Numeric datatype-->int,float,complex along with boolean
#input formatting-->accepting input from the user-->input()
#accepting integer input from user
#by default input() accepts any input
#int(input())-->will accept only integers

age=int(input('Enter the age:24.5'))
print(age)
print(type(age))

age=int(input(bool('Enter the age:25.5;')))
print(age)
prnt(type(age))
#Accepting string input from user
name=input("Enter the name:")
print(name)
print(type(name))

#accepting group of variabes
marks=int(input("enter the marks:")).split()
print(marks)
a=input().split()#by default split() has space
print(a)
#space seperated values
a=input().split()
print(a)'''
'''
#comma seperated values
a=input("Enter the values:").split(',')
print(a)
'''
'''#list of integers
marks=list(map(int,input("enter the values:").split(',')))
print(marks)'''
'''#Now we want to accept 2 values from user
age,salary=(map(int,input("enter the values:").split(',')))
print(age)
print(salary)
'''
'''#single input-->int(input())
#two inputs-->a,b=map(int,input().split(',')
#any number result as list-->a=list(map(int,input().split(',')))
'''
'''#float of integers
marks=list(map(float,input("enter the values:").split(',')))
print(marks)
'''
#Accepting input from user-->int,float-->input formatting

#operating-->operators perform opertions between values(operands)
#7 types-->Arithmetic,assignment,comparison,
#Membership,Identify,Logical,Bitwise
#Arithmetic Opertors-->Arithmetic operators
#+,-,*,%,/
print(7+3)
print(4-6)
print(2%8)
print(9/5)
print(5//10)
a=10
b=7
print(a+b)
#Modulus-->divisble rules-->return remainder
print(5%3)
#Task -->Accept intger input as lrngth,breadth-->fnd the area of rectngle
#Area=length*Bredth
length=16
breadth=52
area=(length*breadth)
print(area)
#assignment operator-->assign the values
#=,+=,-=
a=70
print(a)
#update the value of a
a=a+5#a+=5
print(a)
b=35
b+=a#b=b+a
print(b)
b-=5#b=b-5
print(b)
#Comparison Operator-->we compare the values-->boolen
#==,!=,<,>,=,<=,>=
age=25
print(age==25)#returns the boolean output
print(age!=35)
print(age<=25)
marks=80
print(marks!=80)
salary=-8
print(salary>=-7)
#Membership operartor-->in,not,in-->boolean
#It checks the existence of object in the collection
marks=[40,80,76,90]
print(60 in marks)
#print(35 in 355)#TypeErrror
print(60 not in marks)
print('code'in 'codegnan')

print('sneha' in 'neha')
'''#lgiccal operators-->dcision making-->and,or,not
#and-->all conditions should be satisfied
#or--> any one condition to be satisfed
a=(25 in[25,45,65])and 45>56
print(a)'''
#Identity operator-->check for identity of an objectc-->id()
#is not ,is
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)





