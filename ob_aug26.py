'''
Polymorphism-->It is also one of key feature of OOP,
POLY-->MANY
MORPH-->FORMS
Methods with same name can take diff paramters(argument)
-->Method Overloading(Run-time)
-->Opertor Overloading(+,*)(__add__,__str__)

Hotstar
->Free user-->can watch the movie with advertisments
->PremiumUser-->can watch premium content without
 advertisments
->VIP User-->live cotent,streming quality,premium content


#Method Overloading:

class HotStar:
    """Understanding polymorphism"""
    def watch():
        print(f'User logged into Hotstar..opening hoe page...')
    def watch(self,movie):
        self.movie=movie
        print(f'User watching {self.movie}')
app=HotStar()
app.watch("Leo")
#app.watch() it return error as watch() is overloaded

#1)Method usage with default arguments
#2)Method usage with variable length arguments(*args)
#3)Method usage with type of arguments

class Hotstar:
    """Method Overloding usage"""
    def watch(sef,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print('playing playlist')
            for movie in content:
                print(movie)
obj=Hotstar()
obj.watch("salaar")
obj.watch(["sp",'irumudi','pushpa'])

#metod overriding-->
#It happens in the scenario of Inheritace,where if child  class is
having method name same as parent class thats where  overriding
#we can use super() or if we create diff obj

class FreeUser:
    """Understanding the method overriing"""
    def watch(self):
        print("User logged into Homepage....")
class PremiumUser (FreeUser):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie=movie
        print(f'User watching {self.movie}')
obj=PremiumUser()
obj.watch("salaar")
obj2=FreeUser()
obj2.watch

class FreeUser:
    """Understanding the method overriing"""
    def watch(self):
        print("User logged into Homepage....")
class PremiumUser (FreeUser):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie=movie
        super().watch()
    
        print(f'User watching {self.movie}')
obj=PremiumUser()
obj.watch("salaar")
obj2=FreeUser()
obj2.watch

In above usecase we can create diff obj to access 