'''
Functins-->Arguments usage(variable length arguments)
        -->keyword variabl length arguments(**Kwargs)
        
exception handling/scope of variable/Built-in functions

Exception handling-->It is a mechanism ht elps to respond or make the flow of
execution in normal way,without this error wil occur and disrup the flow of program

common Exceptionns-->ValueError,TypeError,IndexError,AttributeError,ZeroDivisionError..
syntax:
try:
   #code that will cause the exception
except Exceptio as e:
   #code will ctch the excption
finally:
   #runs irrespective of try/except
   ...

#basic Exception handling
try:
    #a=10
    a=int(input("Enter the value:"))
    result=20/a
    print(esult)
#except Exception as e:
    #print(e)#it returns the msg of error
except ValueError:#check by changing case
    print(f'Invalid entry  enter only integer values')
except ZeroDivisionError:
    print(f'Division by Zero is not possible')
except NameError:
    print(f'Check the name of variable properly')
#Similarly we  want to check other Errors-->IndexError,AttributeError,Multiple ExceptionHandling
try:
    a=[10,20,30]
    a.append(24)
    print(a[5])
#except IndexError as e:
    print(e)#returns the message of Error
except IndexError:
    print(f'check the length of the list properly and access elements')
except AttributeError:
    print(f'Dont rush write the name properly')
    
#handling exceptions at a time
try:
    a=[10,20,30]
    a.append(24)
    print(a[5])
except(IndexError,AttributeError)as e:
    print(e)
    a=list(map(int,input("Enter").split(',')))#only for understanding
    print(a)


#BMI-->bmi=(weight)/((height)**2)
#feet-->12 inches-->1 inch-->2.54cm
while True:
    try:
        weight=int(input("Enter the weight in kgs:"))
        height=float(input("Enter the height in metres:"))
        #write my logical condition
        if weight>0 and height>0:
            break#stops te flow of execution of program
            #continue #skips the current itertion nd procced for rmng item
        else:
            print("Make sure to enter only correct values")
    except ValueError:
            print(f'make sure to enter weight as integer only,height also as number')
bmi=((weight)/(height)**2)
print(bmi)
#Use Exception Handling along with Juping Statements in functions BMI
'''
#Scope of Variables-->
#accessible
#Local Scope,Global Scope
#Global Keyword,Enclosing Scope(Nested Functions nonlocal keyword
'''
#Local cope-->Variable defined  inside the function accessible inside

def display():
    """Usage of Local Scope"""
    name='Codegnan'#Local variable
    print(name)
display()

#Global scope(variables)-->Defined outside an cn be accessible anywhere in the script
place="HYD"
def display():
    """usage of Local&Global Scope"""
    name="codegnan"#local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

#Modifying globa variable inside the function and accessible outside te function
count=20
def data():
    """Priority of local vs globl keyword"""
    global count
    count=5
    count=count+5
    print(f'value inside function is{count}')
data()
print(f'value outside fuction is{count}')

#Enclosing Scope (nonlocal keyword)
def outer():
    """Outer function with local variable"""
    count=5
    def inner():
        """Nested Function"""
        nonlocal count
        count=count+10
        print(f'value inside is {count}')
    inner()
    print(f'value outside is {count}')
outer()
'''
#Built in fuctions-->variables BuiltinScoe
len=46
print(len+4)
print(len('codegnan'))#TypeError-->Never ever use Buitin functios as Idntifier














        















    





