'''#sequences-->Strings,Lists,Tuple,set,Frozenset
Mapping-->Ditionary
'''
'''#Set--a set is a unique collection of object,unordered,mutable,Hashing
#set()
#Hashing,Unidexed,Unique,Heterogenous
#set(),{}
a=set()
print(type(a))
stud_ids={123,456,789,876,998}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2])#TypeError
print(234 in stud_ids)
print(stud_ids*2)#TypeeError-->set cant be repeated
print(stud_ids+stud_ids)#TypeError-->Two sets cannot be Merged
'''
'''data={1,2,3,4,5(12,3,4),8}
print(data)#No lists inside a set (hashing technique)as lists are mutble
'''

'''
data={12,3,4,5,(6,8,9),'sneha'}
print(data)
print(len(data))
for i in data:
    print(i)

'''
'''#single element inserting
names={'sneha','devi','codegnan','varshini'}
print(len(names))
names.add('python')
print(names)
#names.add('sneha','poll')
print(names)
names.add(('poll','police'))
print(names)
da_names={'mani','sai','akash','sonu'}
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))
'''


'''
#remove(),discard(),pop(),clear()
#remove() removes an element from the set(it must be a member)
da_names.remove('sai')
print(da_names)
#da_names.remove('sai')#KeyError
#discard()will remove an element if its present else t ignore
da_names.discard('akash')
'''
'''da_names.pop()
print(da_names)
print(da_names.pop())#removes and retirn an arbritary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update(['sai','akash'])
print(da_names)
'''

'''#copy()#create a shallow copy of set (inpendent of each other)
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''


#Mathematical operations-->union(),intersection(),difference(),symmetric_d()
#issubset(),issuperset(),isdisjoint()
da_23={12,23,34,45,23,36}
da_24={34,46,47,23}
#event=da_23.union(da_24)
'''event=da_23|da_24#union()
print(event)
print(len(event))
#common=da_23.intersection(da_24)
commmon=da_23&da_24
#print(common)
#print(len(common))
common=da_23.intersection_update(da_24)
print(common)#it returns None
print(da_23)#ommon elements are finally stored
'''
print(da_23)
print(da_24)
#diff=da_23.difference(da_24)
#print(diff)
#f=da_23=da_24
#print(f)
#symmetric_difference()-->removes common elements and prints all rmng
#elements from two sets
symm=da_23.symmetric_difference(da_24)
#print(symm)
h=da_23^da_24
#print(h)


#issubset()-->checks for all elements to be presen in othr set
da_24.remove(46)
da_24.remove(47)
print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))
#isdisjoint()rturns false for sets havingcommon elements
print(da_23.isdisjoint(da_24))
















