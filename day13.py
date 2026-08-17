#mapping-->Ditionary-->Collection of key-value pairs used o store related data-->Json,API,databse records
'''dict()--> data={}
Dictionary is mutable ,Indexed through keys,Ordered,Heterogeneous
key must be Unique(int,string,float,values..)
'''
details={}
print(type(details))
details={'ID':'CGH4017','name':'sneha',
         'Gender':'F','Age':22,
         'Batch':'DA23','place':'HYD'}
print(details)
print(len(details))

#Access the data fro dictionary
#details[0]#KeyError

print(details.keys())
print(details['ID'],details['name'])
#if key name is not matching/invalid
#print(details['marks'])=#KeyError as marks is notpresent
details['marks']=[]
print('details')
print(type(details['marks']))
details['marks'].append(20)
print(details)
details['marks'].extend([40,45,46,48])
print(details)
#create a key-value pair of practice session
details['PS']=['Tuesday','Thursday','Saturday']
print(details.keys())
#Accessing 3rd day marks os student
print(details['marks'][2])
#Accessing 2nd day of practice session
print(details['PS'][1])
details['MI']=('Monday','wednesday','Friday')
#opearation -->mutable ,Indexing through keys,membership
print('wednesday'in details)
'''
for i in details:
    print(i)#retuns the keys one by one
for i in details.keys():
    print(f'key={i}')
    print(f'Value={details[i]}')
#key()-->return key from dict
for i in details.values():#return value from dict
    print(i)
for i in details.items():#returns a key-value pair in tuple
    print(i)

for key,value in details.items():
    print(f'key is{key}')
    print(f'value is{value}')   
#Update()
details.update({'marks':[],
                'PS':('Tuesday','Thursday','Saturday')})
print(details)
#details['marks'].extend([25,30,25])
#print(details)
marks=list(map(int,input("Enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)
'''
print(details.keys())
print(details.get('name'))
print(details.get('Branch'))#it return None as we dont have branch as key
print(details.keys())

details.setdefault('Branch')#if key is not present in inserts into dict
print(details)
details['Brach']='CSE'
print(details.setdefault('name'))
print(details.keys())
print(details.pop('Branch'))#we need to mention key
print(details.keys())
print(details.popitem())#removes and return a key,value pair as a  2 tuple
print(details.popitem())
del details['ID']
print(details.keys())
details.clear()#remove all elements from D
print(details)
#fromkeys()
data=['sai','data','mani']
b=dict.fromkeys(data)#create a dict but values set to None
print(b)
b['sai']=31
print(b)
c=dict.fromkeys(['CGH1234','CGH2345',],['CODE','GNAN'])
print(c)
#Task:Create a dictionary with your personal details,similar to your
#Codegnan Profile














