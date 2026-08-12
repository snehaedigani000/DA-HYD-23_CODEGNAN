
'''
sequence->strings,lists,tuple,sets
Mapping-->Dictionary
'''
'''#Lists-->Collection of heterogeneous elements
#List--Indexed,ordere,Mutable,Heterogenous[]to store the data
marks=[35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
'''
'''#Operations:Indexing,Slicing,Striding,Membership,Merging,Repetition
#Nested list-->A list inside another list
names=['codegnan',5,4.7,[67,86,87,99],'Day23',87]
print(len(names))
print(names[0])
print(names[-5])
print(names[-3])
print(type(names[0]))
print(names[0][:4])#it returns the code
print(names[0][4:])
#get the output as cdga
print(names[0][::-1])
names[0]=names[0][::-1]
print(names)
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing slicing-->Multiple
names[2]='python'
print(names)
#by indexing if we change the elements length of collection will remain same
names[4]=['codegnan',25,'python',[67,86,87,99],'Day23',87]
print(names[4][0][4:])
names[2:4]='sneha','nagadevi'
print(names)
#I slicing whatever elements u pass as per te logic length keeps on incresing
#o/p as follows:
#['codegnan',25,'sneha','python','nagadevi','java','Day23',34]
names=[3:6:2]=['c','java']
print(names)
#create a nested list with strings,lists an work on Indexing,slicing,striding
#added advantages if u could add string functions also to it
'''
#Lists function-->append(),insert(),extend(),pop(),remove(),clear()

#idex(),count(),copy(),sort(),reverse()


names=['codegnan','sneha']
names.append('data')
print(names)
names.append(['analysis','agent'])
print(names)
#append will always increment the length of ist by 1
print([3])
names[3].append('chatgpt')
print(names)


#extend()--->inserts multiple elements to the end of list
names.extend('analysis')#string wi be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#insert(insert,object)-->insertts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b'])#SYNTAX ERROR
#print(names)
names.insert(-1,'AAA')
print(names)
#pop(),remove(),clear()
#pop() by default last,else given indx
print(names.pop())
print(names)
names.pop(2)
print(names)

#remove() we can move  specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
#names.remove(14)#it raises Valueerror
del names[1:3]#del keyword will apply permanent changes
print(names)
names.clear()#clear() will remove all elements and  return empty list
print(names)
#data=['codegnan','sneha','python','java']#input
#output should be as follows
'''
0:codegnan
1:sneha
2:python
3:java
'''s































