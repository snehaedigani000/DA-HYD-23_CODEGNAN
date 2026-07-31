'''
Identity Operators-->checks the identity of an object-->id()
'''
'''a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
c=5
print(id(c))
print(a is c)
print(5==5)
'''
'''a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#as we have list(Mutuble Collection)
#iss whereas values are same
print(c is a)#output false
print(c==a)#output true
print(a is not c)
'''
'''#Biwise opperators-->we  perform bitwise operations over operands
#$,|(or),^(xor),shifting operators(<<,>>)
#Numbe will be converted to binary format
print(5&3)#both 5 and 3 to be converted binary and bitwise is performed
print(5|3)#bitwise OR
print(5^3)#BItwise XOR
print(5 and 3)#here and is logical operator checks for both existences
#return 5 in above casse
print(5 or 3)#returns 3 in this case'''
#Leftshift operator<<,Right shift operator>>
print(5<1)#convert 15 to binary and perfrm 2 time left shifting
print(5<<1)#same 2 times right shifting
'''#Iput formattting-->input(),int(input()),float(input))
#you know -->single input-->
#2 or 3 inputs-->map()
#grioup of integers -->list(map,(int,inpu().split(','))
name=input("enter the Friends Names;",).split(',')
print(name,name)
'''
'''#Tokens-->Numeric Datatypes->Operators-->flow of the program
#contol Block statemnt--they control te flow of te program
#when to execut,how to execute
#Conditinal ststements-->if,else elifrelay on condition   to be execurd )
Syntax:

if<condition>
  statement(s)...
  .....
  '''
'''
#age=15
age=int(input("enter th age:"))
if age>=18:
   print('Your age is:',age)
   '''
'''age=int(input("Enter the age:"))
if age>=18 and age in[19,21,20]:
   print('your age is',age)
   print(age)
  ''' #else keyword-->if-else
'''
   '''
'''else:
       statement(s)...
if else usage as below:
    if<conition>:
        statement(s)...
        ...
else:
    statement(s)....
    '''
'''
#Vote eligibility-->To check his/her voter eligibility and give access
age=int(input("Enter tge age:"))
if age>=18:
   print("you have vote eligibility and age is",age)
   print("access Granted")
else:
    age=18-age
    #print("Y0u dont have eligibiity as your age is",age,"years")
    print("You need to wait for more",age,"years")      
'''
    
'''
task: student marks and grade analyzer
90-100 --->'A'
80-89----->'B'
70-79 ---->'C'
60-69---->'D'
>60 -->fail
#also -ve cases should not be allowed and marks should not greater 100
