import ob_aug29
print(dir(ob_aug29))
print(type(ob_aug29.details))
print(type(ob_aug29.greeting))
print(ob_aug29.greeting())
print(ob_aug29.details)
#we can access functions/datatpes uing. operator
ob_aug29.details['subjects']=['python','sql','EDA','powerBI','excel']
print(ob_aug29.details.keys())
#we can use from keyword to access desired methods/datatypes
'''from ob_aug29 import details
print(details)
#print(greeting()) as we didnot import it raises NameError
details['subjects']=['python','sql','EDA','powerBI','excel']
print(details)
#we want to acces group of methods/datatypes we can use comma
from ob_aug29 import details,greeting
print(greeting())
print(details)

# you want to access all funcions from a module at a time
from ob_aug29 import *
print(details)
print(greeting())

#Aliasing-->we can use as keyword as shortcut for original file
import ob_aug29 as mod
print(mod.details)'''

#we will work on some built-in modules-->random,math

import random
import time
#random module-->get random number generation,random,texxt
print(dir(random))
#OTP generation
print(random.randint(1,10))
'''for i in range(5):
    print(random.randint(1000,9999)) # start limit,endlimit
    time.sleep(5)#delays execution sleep(seconds)

print(random.random())#returns a float value of random


details=['A long back','once upon a time','Appatlo','ten years']
print(random.choice(details))

#You can try for story generation
'''
#math module-->mathemtical constant,log,exp,trignometric.
import math
print(math.ceil(4.5))
print(math.floor(4.78))
print(math.factorial(5))
print(math.pi)