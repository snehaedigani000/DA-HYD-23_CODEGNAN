'''
Tokens--> variables,punctuaors
variables--> named memory location,its a placeholder for data
#rules are to be followed
'''
#multiAssignment of variabls
name,age,place='codegnan','7','hyd'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='--->')
#a,b= 2,4,5 #valueErrors as too manyvalues to unpack
#Reassigning vriables
name="codegnan"
a,b=45,1.5
print(a,b)
a,b=b,a
print(a,b,sep=',')
#a,b=b,c #NameError as c is not defined
#print(a,b)
#Deleting the varibles -->del
#del a
#print(a)
#del a,b
#print(a,b)
#puctuators --> [](Lists),()(Tuple),{}(Dict,Sets)
name="codegnan";age=7;course='Data_Analysis'
print(name,age,course)
#Datatypes --> Numeric (int,float,complex),boolean,None,
         #-->Sequences-->List,Tuples,Sets,String,
             #         Frozensets,mapping(dict)
#Numeric type -->int,float,complex
#int datatype -->quantity,age..
age=7
print(age)
print(type(age)) #type -->returns the datatype of object
print(type(234))
'''
#quantity =03 # it is not allowed
#print(quantity)
#float datatypes -->temp,salary,price
price=750.24;discount =2.5
print(price,discount)
print(type(price))
'''
#complex -->combination of real and img
i2=4
data=5+i2
print(data)
data=5+2j #j is img representation
print(data)
print(type(data))
#Boolean-->True/False
valid=True
print(type(valid))
error=False
print(type(error))

#Typecasting-->converting one type to another type
#python by default f0llows Implict Type (we need not mention datatype)
#we will go for explict  conversation
#every built-in datatype is a buil-in function
int,float,complex,bool
#TypeCasting-->int-->float,complex,bool
age=35
print(type(age))
b=int(age)
print(b)
c= int(age)
print(c)
d=float(age)
print(d)
e=bool(age)#returns True for exisiting data
print(e)
#complex-->TypeCasting-->int,float,bool
data=2+5j
print(type(data))
#b=int(data)#TypeError
#print(int(data))
#print(c)
d=bool(data)
print(d)
print(type(d))
e=int(float(bool(45)))
print(e)
e=bool(int(float(23)))
print(e)
f=45+2.5+2+3j+False
print(f)

#

