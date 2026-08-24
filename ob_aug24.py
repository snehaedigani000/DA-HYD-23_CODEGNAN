'''
OOP-->CLASS,OBJECT,METHOD(__init__())
Encapsulation-->Public,Protected,Private
Inheritance-->It is one of key feature of oop where we inherit the
properies(attribute/method) from on class to  another
class(base class(parent class)-->derived class(Child class)
Whatsapp-->Personal User,Business User(Catalog) community add
Features-->Code Reusability,Avoiding Code Duplication,
Code Maintainability,Polymorphism(Method Overriding,
Method Overloading,Operator Overloading __add__,str__)

Types: Single Inheritence(Finger print)
-->One child class inherting properties 
from one parent class
Multiple Inheritence(Mother,Father-->Chid)-->One child class
inherting properties from two parent classes
Mutilevel Inheritance(GrandParent-->Parent-->Child)
level by level
Hierarchical Inheritence-->multiple child clsses 
inheriting proprties from single parent
Hybrid  Inheritance-->It can carr oe or more type of inheritance


syntax:
Single Inheritance:

class baseclass:
    statement(s)...
    ......
class Derivedclass(baseclass):
    .......
    .......

#Whatsapp Scenario-->Personal User

class User:
    """Single Inheritace usage"""
    def send_message(self):
        print('Sending Message')
    def voice_call(self):
        print('Making voice calls')
    def video_call(self):
        print("making video calls")
class BusinessUser(User):
    #pass
    def create_catalog(self):
        print("Displaying Products Catalog")
u1=BusinessUser()
print(dir(u1))
u1.send_message()
u1.video_call()

#SocialMedia Login-->user-->update_users
class Users:
    """Single Inheritance  usage"""
    company="codegnan"
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname+self.lname
#u1=Users("sneha","Edigani")
#print(u1.full_name())
#print(u1.company)
class update_users(Users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1=update_users("sneha","Edigani")
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2=Users("naga","jyo")
print(u2.full_name())
print(u2.company)

#what if we have constructor in child class also...
#Father-->Kid(property)
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property=1000000
    def father_property(self):
        print(f'Father property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now childcase will have Constructor"""
    def __init__(self):
        self.cash=2000000
    def Kid_cash(self):
        print(f'Kid cash is {self.cash}')
obj=Kid()
obj.father_property()
obj.Kid_cash()
#parent class is ha ving constructor child class is having constructor child class is overloading
#To avoid overriding we start using super()
#super().__init__()
#super().__init__(args)
#super().method()-->Method Overriding
'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property=1000000
    def father_property(self):
        print(f'Father property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now childcase will have Constructor"""
    def __init__(self):
        super().__init__()#calling superclass constructor
        self.cash=2000000
    def Kid_cash(self):
        print(f'Kid cash is {self.cash}')
        print(f'Kid Final Property{self.cash+self.property}')
obj=Kid()
obj.father_property()
obj.Kid_cash()




