'''
#super method()


class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self,property):
        self.property=1000000
    def father_property(self):
        print(f'Father property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now childcase will have Constructor"""
    def __init__(self,cash,property):
        self.cash=cash
        super().__init__(property)
    def Kid_property(self):
        print(f'Kid cash is {self.cash}')
        print(f'Kid Final Property{self.cash+self.property}')
obj=Kid(250000,1000000)
obj.Kid_property()
obj.father_property()

#whatif child class  is having same metod name as
#parent class-->method Overriding
#Area of Square/Rectangle

class Square:
    """Method Overriding Usage"""
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of Square is {self.x**2}')
class Rectangle(Square):
    def __init__(self,x,y):
        self.y=y
        super().__init__(x)
    def area(self):
        super().area()
        print(f'Area of rectangle is {self.x*self.y}')
x,y=map(int,input("Enter the values:").split(','))
obj=Rectangle(4,3)
obj.area()
'''
#Mutliple inheritance
'''
class parent1:
    .....
class parent2:
    .....
class child(parent1,parent2):
    .....

class User:
    """First parent class with user features"""
    def voice_call(self):
        print('Making Voice calls')
class Notifications:
    def notification(self):
        print("sending Notifications")
class PremiumUser(User,Notifications):
    def verification_badge(self):
        print("Blue Tick Verification done")
user=PremiumUser()
user.verification_badge()
user.voice_call()
user.notification()
'''
'''
#Multilevel Inheritance

class Grandparent:
    ....
class parent(Grandparent):
    ....
class child(parent):
    ....
'''
class User:
    def voice_call(self):
        print('Making Voice calls')
class BusinessUser:
    def Catalog(self):
        print("displaying the items")
class VerifyBusinessUser:
    def Verification_badge(self):
        print("Bluetick verification")
obj=VerifyBusinessUser()
obj=BusinessUser()
obj=User()


