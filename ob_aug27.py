'''#Operator overloading -->Operator(+,-,*,/)-->Operator will behave
in a diff way as per user defined o bjects...

#+(Addition,Concatenation,Merging)

print(3+2)#addition
print('code+gnan')#concatination
print([3,45]+[4,5])
#print(3.__add__(4)#__add__(self,other)
a=25;b=3
print(a.__add__(b))
a=[12,3,4,];b=[3,4,5]
print(a.__add__(b))#merging
print(a.__len__())#len(a)
print(a.__mul__(2))#print([12,3,4,4]*2)

#lets apply the above scenario history WatchHistory

class WatchHistory:
    """Define the no of hours"""
    def __init__(self,hours):
        self.hours=hours
sneha=WatchHistory(100)
print(sneha.hours)
akash=WatchHistory(120)
print(akash.hours)
#pint(sneha+akash)
print(sneha.hours+akash.hours)
'''
#But the prefarble way is usage of __add__
class WatchHistory:
    """Define the no of hours"""
    def __init__(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
        return (f'WatchHistory is {self.hours}')

varun=WatchHistory(300)
print(varun)
print(varun.hours)#__str__method
akash=WatchHistory(50)
print(akash)
print(akash.hours)
print(varun+akash)
   


