'''
#Task
marks=int(int(input("marks(1-100):")))
if marks>0 and marks<=100:
    if marks>=90:
       print("User has secured Grade A")
    if marks>=80 and marks<=89:
       print("User has secured Grade B")
    if marks>=70 and marks<=79:
       print("User has secured Grade C")
    if marks>=60 and marks<=69:
       print("User has secured Grade D")
    if marks<60:
        print("user has failed,study again")
else:
    print("Enter only+ve values greater than 0 and  less tha 100")
'''
'''#elif keyword --> if-elif-else
       
marks=int(input("Enter the Student marks:"))
if marks>=100:
   print("Entered the values should br grater than 1 and less than 100")
elif marks>=90 and marks <=100:
     print("User has secured Grade A")
elif marks>=80 and marks<=89:
     print("User has secured Grade B")
elif marks>=70 and marks<=79:
     print("User has secured Grade C")
elif marks>=60 and marks<=69:
     print("User has secured Grade D")
elif marks<60 and marks>=0:
     print("user has failed,study again")
else:
     print("No negative values")
'''
'''# Voter eligibility checkcase-->make sure to satisfy all possible conditions
#>=18-->Accesss
#<18-->no of years eligibility should tell
#negative values -->not accetpable
age=int(input("enter the age:"))
if age>=18 and age<=100:
    print('-----user has votr eligibiity---')
    print('---access granted---')
elif age<18 and age>0:
    print('---user still need to get vote eligibility---')
    print('---user need to wait for more',(18-age),'year(s)---')
else:
    print('---only +ve values and less than 100 acceptable---')
#prefer if elif else
'''
'''#Output formatting-->od styl formatting (using commas)
#%usage (%f,%d),format() usage,fstring notatio
a,b=7,9
print(a)
print(b)
print(a,b)
name="Codegnan";batch="Data analyst"
print(name,batch)#by defaulbby having space
print(name,batch,sep=',')
print(name,batch,sep='------->')
#end='\n',\t-->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("Hyderbad")
'''
name='codegnan';age=7;batch='DA-023';place='HYD'
print(batch,'is in',name)
print(name,'is in',place,'age is',age,'years')
#old style formatting -->%d -->integer,%s-->string,%f-->float
salary=25000.256
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.2f"%(salary))#%.1f-->rounding to 1 decimal
#.format()usage
print("{}is in{}".format(name,place))#order matters
#fstring usage (more recommended)
print(f'{name} is in {place}')
print(f'{"sneha"} is in {"HYD"}')



