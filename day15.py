'''
Functios-->Variable length arguments(*args)
        -->Keyword variable length arguments(**kwrgs)
Variable length arguments-->The no of positional arguments are not limit,we can pass any no of arguments,but we can
pass any no of arguments,but we need to use* representation,data is stored in tupl

def sample(*args):
    """Simple demo for *args"""
    print(args)
    print(type(args))
sample()
sample(1,3,5,6)
sample('Codegnan','sneha',23)
details=[24,45,35,65]
sample(details)#Passing a collection
sample(*details)#unpacking values from collection

a,b,c=13,4,'da'
print(a,b,c)
#a,*b,c='python','codegnan',23,45,9.7,'data'
#a,b,*c='python','codegnan',23,45,9.7,'data'
a,b,*c=34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,34,6,7])
print(c)

#Task-->we wnted to calculate the sum of given objects usig Function
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result=0
    for i in a:
        #print(i)
        #if type(i)==int or type(i)==float:
        if type(i) in (int,float,complex):
            #print(i) 
             result=result+i
    return result     
#print(add())
#print(add(12,3,4,5))
#print(add(12,3,4.5))
#print(add(3,4,5,'poll','dear',4.5))
#print(add(3,4,5,+24j,'poll','dear',4.5))
b=list(map(int,input("Enter the values:").split(',')))
print(*b)#it returns each value side by side
for i in b:
    print(i,end=' ')#same as here
#keyword variable length argument-->we can pass any no of keyword argumens we use ** representation
#data is stored in dict

def details(**Kwargs):
    """usage of **Kwargs demo"""
    print(Kwargs)
    print(type(Kwargs))
details()#return empty dictionary
details(name="Codegnan",place="HYD",batch="da")
batch={'number':'da23','plac':'hyd'}
details(**batch)
'''
#Now let us include both of thm into a function
def sample(*a,**b):
    """usage of both variabl lngth ad keyword variable length args"""
    result=0
    for i in a:
        if type(i) in (int,float,complex):
            result=result+i 
    print(result)
    for key,value in b.items():
        print(f'key is{key}')
        print(f'value is {value}')
sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="HYD",
       batch="da23")
#sample(name="codegnan",23,ids=23455)#positional args follows keyword args
       
              































