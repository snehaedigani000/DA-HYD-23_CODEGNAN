'''
Constructor --> Instance methods -->Public Attributes
Encapsulation
Constructor --> It is a special method(__init__())
which will automatically intialize the attributes and the method to the object in the class

class Car_Brand:
    """Understanding the usage of constructor in oops"""
    def __init__(self,brand,model,price,color):
        self.brand=brand
        self.model=model
        self.price=price
        self.color=color
    
    def display(self):
        print(f'The car brand is {self.brand}')
        print(f'The car model is {self.model}')
        print(f'The car price is {self.price}')
        print(f'The car color is {self.color}')
b1=Car_Brand("Tata","Nexon","9lakh","Blue")
b1.display()
print(b1.__dict__)
b2=Car_Brand()

class Car_Brand:
    """Understanding the usage of constructor in oops"""
    def __init__(self):
        self.brand="BMW" #public attributes
        self.model="Sedans"
        self.price="50lakh"
        self.color="Blue"
    
    def display(self):
        print(f'The car brand is {self.brand}')
        print(f'The car model is {self.model}')
        print(f'The car price is {self.price}')
        print(f'The car color is {self.color}')
b1=Car_Brand()
print(b1.brand,b1.model,b1.price,b1.color)
b1.display()

Encapsulation-->It is  one of the main feature of oops
it binds(bundles)the data(attributes)and the methods(Behaviour)
into a single unit(class)-->multipe objects
-->Attribute-->public,protected,private
#public attribute-->Attribute defined inside the class
and can be modified outside the class

class CodegnanPortal:
    """Codegnan portal with users"""
    def __init__(self,username):
       self.user=username#Public attribute
    #To access student details
    def display(self):
        print(f'student Userame is {self.user}')
u1=CodegnanPortal("sneha")
u1.display()
u1.user="sneha"
u1.display()
print(u1.__dict__)
u2=CodegnanPortal("jayachandra")
u2.display()
print(u2.__dict__)

#protected attributes-->we can use single underscore before an
#attribute moreover it can be modified also outside the class
#and even accessible subclasses...
class CodegnanPortal:
    """Codegnan portal with users"""
    def __init__(self,username,_otp):
        self.user=username
        self._otp=_otp#Public attribute
    #To access student details
    def display(self):
        print(f'student Username is {self.user}')
        print(f'student has received OTP as {self._otp}')
u1=CodegnanPortal("sneha")
u1.display()
u1._otp=3456
u1.display()
'''
'''#Private  Attribute--> we use special notation as doubleunderscore
#such as password
#Accessible only inside the class and cannot be directly
'''
'''
class CodegnanPortal:
    """Codegnan portal with users"""
    def __init__(self,username,_otp,password):
        self.user=username
        self._otp=_otp#Public attribute
        self.__password=password #private attribute
#To access student details
def display(self):
    print(f'student Username is {self.user}')
    print(f'student has received OTP as {self._otp}')
u1=CodegnanPortal("sneha",3456,"admin123")
#print(u1.CodegnanPortal.__password)#NameMangling
print(u1.__dict__)
# in above case we are using NameMangling but the right way is
# #usage of getter()  and setter() methods            
'''
class CodegnanPortal:
    """Codegnan portal with users"""
    def __init__(self,username,_otp,password):
        self.user=username
        self._otp=_otp#Public attribute
        self.__password=password #private attribute
    #Usage of getter() method
    def get_password(self):
        return self.__password
    #To modify the password we use setter() method
    def set_password(self,new_password):
        if len(new_password)<6:
            print("Wrong password not satisfied 6 characters")
        else:
            self.__password=new_password
            print("Now password is updated")
u1=CodegnanPortal("sneha",23456,"admin123")
print(u1.get_password())
u1.set_password("sneha")
u1.set_password("sneha123")#compulsory morethann 6
print(u1.get_password())