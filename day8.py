'''#Strings--.Group of characters,we use single or double or triple quotes
#for representation of strings..
#strings are Immutable,Ordered,Indexed Collection
name="Codegnan"
print(name)
print(type(name))
print(len(name))#len-->returns the no of items i a container

#Index()->fetch the object(position) starts at 0 and ends at len(obj)
print(name[0])
print(name[6])

#Negative Indexing-->-1 to len(obJ)
print(name[-1])
print(name[-7])
#slicing-->we can access the group of characters (objects)
#we use[start:end]#start default-->0,start is includd,end is exculdd
print(name[:])# we get entire codegnan
print(name[0:])#returns entire string
print(name[:4])#start  at 0th index before 4th index
print(name[1:5])                   
print(name[-4:-7])#returns an empty string becz string is ordered
'''
'''#slicing is applicable from lower to higher index
name='python'
print(name[3:7])
print(name[45:])
print(name[-5:-1])#start at-5 and ends at-2
print(name[-2:])
print(name[1:-2])
print(name[2:-3])
#observe +ve ,+ve ,-ve,-ve and all possible
#string-->[start:end:step]
course='DataAnalysis'
print(len(course))
#Data-->result
print(course[:4])
print(course[-3:])
print(course[::1])#returns all characters
print(course[::2])#includes start to end skipping1 character
print(course[1:6:3])#[1:6]ataAn-->[1:6:3]-->aA
print(course[2::3])#tnys
print(course[::-1])
print(course[::-2])
#task:Workout with all possibilities of slicing and striding on a example
name='codegnan'
#name[3]='w'#string are immutable

#operators on strings-->Indexing,concatenation,Repetation
print(name*3)
print('*'*25)#repettion
#cocatenation-->Combination strings

data='sneha'+'Python'+'database'
print(data)
print('123'*4)
print('code' in 'codegnan')
for  i in 'codegnan':
    print(i,':')
#in above case we get every line by line
for i in 'codegnan':
    print(i,end=',')
'''
'''name="DataCodegnan"
#Built-in functions-->len(),min(),max(),sorted()
print(len(name))
print(min(name))#alphabetical order ASCII ordering
print(ord('C'))
print(ord('a'))
print(max(name))
print(chr(97))
print(sorted(name))#returns a list by sorting all elements
'''
#Methods on string-->Case-conversion,Finding/Searching.....
name='CodEgnan data'
#case-Coversions->upper(),lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)
#Captalize()-->converts first letter to uppercase
c=name.capitalize()
print(c)
d=name.title()#coverts every work firs letter to uppercase
print(d)

#task :A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#USE loops and strings to return A-Z


