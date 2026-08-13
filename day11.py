'''
lists,Tuples..
'''
'''#list-->Mutable,ordered,Heterogenous
#index(),count(),copy(),sort(),reverse()
details=['codegnan',7,2018,'HYD']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))
print(details.index(21))#it returns first occurance
print(details.index(21,6))
#print(details.index('pyton'))#valuError
print(details.count(21))
print(details.count('python'))#it returns 0 as we dont have it
'''
data=['codegnan','sneha','python','java']
#output should be follows
''''0:codegnan
1:snha
2:python
3:java

for obj in data:
    print(data.index(obj),':',obj)
for obj in range(len(data)):
    print(obj,':',data[obj])
'''
#copy()-->shallow copy of the given collection
'''new=data.copy()
print(new)
print(type(new))
print(len(data))

new[2]='Agentic AI'
print(new)
print(data)
data.append('devi')
print(data)
print(new)
new[3]='hy'
print(new)
print(data)
'''

'''data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)
new[3][2]='agents'#whenever we make changes in nested lit originl wil also be affected
print(new)
print(data)
new[1]='python'
print(new)
print(data)
'''
'''marks=[14,24,-45,27,35]# str is added it will raise as TypError
print(marks)
print(marks.sort())#returns None
print(marks)#retur in ascending order
marks.sort(reverse=True)#returns in Descning oredrr...
print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse()-->returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])# reverse order
print(marks[2:])
 #type(),len(),max(),min(),print()
print(sorted('codegnan'))#returns list in ascending oredr
#print(sorted(]'code',23,34,51]))#raise error
'''

'''
#Tuple-->Tuples are indexed,ordered,Heterogenous,Immutable collection
#dimension,coordinte,database records we prefer() for tuple notat
a=()
print(type(a))
print(len(a))
dimensions=1.5,2.6
print(dimensions)
print(type(dimensions))
print(len(dimensions))
#Operations-->Indexing,slicing,striding,membership,merging,repetition
courses=('pfs','jfs',('DA','DS'),'AgenticAI',[100,6,6])
print(courses)
print(len(courses))
print(courses[-2][-2:])
#courses[2]=23#tuples are immutabbble
courses[-1].append('codegnan')#we can make any modifications inside list
print(courses)
#create a Nested tuple as above and work on slicing,stridig and list function

print('PFS' in courses)#membership
d=courses*2#repetition
print(d)
e=courses+(2,3,4,5)#merging
print(e)
#Tuples immutabble-->count(),index()
print(courses.index('AgenticAI'))#return first occurance
#print(coursessort())#AttributError-->sort()in lists not in tuples
#print(sorted(courses[-1]))
#prited(sorted(courses))#as we have mixe type
#TypeCasting
d=tuple(sorted((23,12,3,4,5)))
print(d)
'''

#accept group of integers space seperated
a,b=map(int,input("Enter the value:").split())
print(a,b)
a= tuple(map(int,input("Enter he values").split(',',)))
print(a)
print(9+4)
#eval() func can take any kind of input
print(eval('9+4'))
a=eval(input("Enter a lis:"))#in this case u can exactly enter data as list
print(a)
print(type(a))












