'''#Strings-->caseconversions,searching&finding,string,testing methods,replce,spac removal
#Searching,finding,Replacing,Joining...
a="Codegnan"
print(len(a))
print(min(a))
print(max(a))
b=a.index('g')#it returns the index position
print(b)
c=a.index('n')#it returns only the first occurace
print(c)
d=a.index('n',6)#it returns the next occurace
print(d)
#e=a.index('n',8)#value Error
#print(e)
#f=a.index('t')#valueError
#print(f)
g=a.index('n',1,4)
print(g)
'''
'''
#rindex()-->returns last occurance
b=a.index('g')
print(b)
c=a.rindex('n')
print(c)
#d=a.rindex('n',8)#it returns the valueerror
#print(d)
'''
'''#count)--> returns the number of items object is repeating
print('Codegnan'.count('n'))
print('code'.count('w'))
print('Caskshjasakajs'.count('a'))
'''
'''#find()->First occurance but it avoud error returns -1 is substrig is not found
print('codegnan'.find('r'))#it returns-1

print('codegnan'.find('n'))

print('codegnan'.rfind('n'))
'''
'''a="DataAnalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))
'''
'''#Replacing,spliting,joining
#Strings are immutable
a="Codegnan"
#a[4]='s'
print(a.replace('g','s'))
a=a.replace('g','s')
print(a)
print('fefvyuvhugv#vgfcg5r2#nmasam'.replace('#',''))
print(a.replace('x','sneha'))
'''
'''a='code sneha python'
b=a.split()#default if it have space it splits
print(b)
print(len(b))
c='code,saketh,python'
d=c.split()
print(d)
e=c.split(',')
print(e)
'''
'''#Join(Iterable)-->concatenate any no of strings
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('sneha'))
print(' '.join(sneha))
'''
'''#String testing methods(boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower().....
a='Codegnan123'
print(a.isalnum())#Returns truce for alphanumeric strings else false
b='Codegnan'
print(b.isalnum())
print(b.isalpha())#returns the True only for alhabets
print(b.isdigit())
print('566442466'.isdigit())
print('2345'.isnumeric())
print('codegnan'.startswith('g'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
'''
print('Sneha'.islower())
print('Sneha'.isupper())
print('Sneha yadav'.istitle())
#Space removal-->strip()( removes leading and trailing spaces)
a="  Codegnan"
print(a.strip())
b=input("Enter the string:".strip().lower())
print(b)
























