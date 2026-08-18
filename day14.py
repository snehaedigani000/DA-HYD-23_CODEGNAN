'''
Tokens,DataTypes-->Cotrol Flow statement-->if,else,else,for while,break,continue..
Procedure Oriented Programming
Function-->A Function is a block of code which performs a specific task
Its a reusable group of statements where we define using def keyword
Advantages-->Code reusability,code maintainability,ease of debugging voiding code duplication

def fname(parameters):   def func
    """ Doc String """ Description
    statements(s)....
    .........
    return value(s)....
fname(args)   function call
'''
'''#To perform sum of given objects
def add(a,b):
    """sum of objects"""
    c=a+b
    return c
print(add(12,3))#Addition
print(add('code','gnan'))#cancatenation
print(add([12,5],[12,34]))#merging
c,d=map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34))#it returns None 

name,age,salary="sneha",22,50000

#usage of return
def details():
    return name,age,salary
    #return #whatever  we give to return it gives same
print(details())

there are 5 types of arguments:
-->Poitional Argument
-->Default Argument
-->keyword Argument
-->keyword variable length arguments(**kwargs)

#positional Arguments-->Number of arguments in function defn should match with func call(order has to be maintained)
#print(len(123,234)this is as  per built in len(obj)will accept one argument
def details(name,place):
    """To store the details"""
    #name="codegnan"
    #place="HYD"
    return name,place      
#print(details("codegnan","HYD"))
#print(details("sai","mani"))
#print(details("sn","kl",23))#raise TypeError as only 2 arguments are given
c,d=map(str,input("enter the values").split(','))
details(c,d)

#Default arguments-->we can make arguments as default but no first arguments as default
def grocery(item="Cheese",price=100):#we can also make all args as default
    """usage of default arguments"""
    print(f'the Item is{item} and price is {price}')
grocery("milk",32)
#grocery(32,"milk")
grocery("Bread")#by default we have  given price as 35
grocery()#as both item and price as default arguments
'''

#keyword arguments-->Whenever we want to specify the names pf argument
def employee(name,salary,role,place="Codegnan"):
    """keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is salary{salary} works in {place}')
employee("sneha",20000,"Admin")
employee(salary=25000,role="Frontdesk",name="Asha")
employee("Akash",250000,"IT","cognizant")






















        

