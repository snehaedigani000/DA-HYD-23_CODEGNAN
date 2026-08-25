'''
oop --> object oreiented programming
--> Attributes(Data),Methods(Behaviour)
class,object -->A Class is a blueprint(template) for an object
An object oreiented programming is a mechanisim or a proceducure or process which revolves around creating the object consist of attributes (which are variables which carry the data to the class),
Method(a method is a function  defined  inside a class which carry the behaviour of object)
Example:
Chair(object)--> Wood,Tools,Dimensions(blueprint),Carpenter
Features of OOP -->Modularity,Scalability,Encapsualtion(biniding the data(attributes),
features to the class) (objects)
Abstraction -->Show only relevant infromation to the class()
Inheritance -->Acquring properties(attributes,methods)
Single -->Fingerprint
Multiple --> Parents(Mother,Father)-->Child
Multilevel -->Grandparent -->parent -->child
Polymorphism -->Methods Overlodaing,Overriding,operator Overridding
'''

#Syntax for class creation
'''
class Class_Name:
    """Doc String"""
    attributes (characteristics)
    ...............
    def func(self): (behaviour)
        ........
        .......
    ........  
obj=Class_Name()

#Student Class with basic details
class Student :
    """Understanding the usage of oop"""
    name="Sneha"
    id="CGH4022"
    gender="female"
    email_id="sneha@gmail.com" 
    #Methods(behaviour)
    def display(self):
        print(f'student name is{self.name}')
        print(f'student ID is {self.id}')
        print(f'student Mail id is {self.email_id}')
u1=Student()
print(u1)
print(dir(u1)) #directory (returns all available methods/)
u1.display()
u2=Student()
u2.display()

#Student class for multiple objectss
class Students :
    """Understanding the usage of oop"""
    name=input("Enter the name:")
    id=input("Enter the ID No:")
    gender=input("Enter the gender:")
    email_id=input("Enter the email_id:")
    #Methods(behaviour)
    def display(self):
        print(f'student name is{self.name}')
        print(f'student ID is {self.id}')
        print(f'student Mail id is {self.email_id}')
u1=Students()
print(u1)
u1.display()
u2=Students()
u2.display()
print(u1.__dict__)
print(u2.__dict__)

#Students details with multiples objects
class Students :
    """Understanding the usage of oop"""
    def data(self,name,id,gender,email_id):
        self.name=name
        self.id=id
        self.gender=gender
        self.email_id=email_id
    #Methods(behaviour)
    def display(self):
        print(f'student name is{self.name}')
        print(f'student ID is {self.id}')
        print(f'student Mail id is {self.email_id}')
u1=Students()
u1.data("Sneha","CGH4022","female","sneha@gmailcom")
u1.display()
print(u1.__dict__)
u2=Students()
u2.data("Akash","CGH4023","male","aksha@gmail.com")
u2.display()
print(u2.__dict__)
'''
#Create a class with Car Brand name,price,color --> display()

class Car:
    """Understanding the usage of OOP"""

    def data(self, brand, price, color,model):
        self.brand = brand
        self.price = price
        self.color = color
        self.model = model
    def display(self):
        print(f'Car brand is {self.brand}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
        print(f'Car model is {self.model}')



c1 = Car()
c1.data("Toyota", 2500000, "White","glanza")
c1.display()
print(c1.__dict__)

c2 = Car()
c2.data("BMW", 5500000, "Black","glanza")
c2.display()
print(c2.__dict__)





