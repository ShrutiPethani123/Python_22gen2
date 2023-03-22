l1 = [2,4,5,6,7]
print("list1:",l1)

l2=l1.copy()
print("list2:",l2)

l3=l1
print("list3:",l3)

l3[2]=23
print(l1,id(l1))
print(l3,id(l3))
print(l2,id(l2))

# identity operator: is ,  is not

print(l1 is l2)
print(l1 is l3)


print(l1 is not l2)
print(l1 is not l3) 


l2.clear()
print(l2)

# del l2
# print(l2)

print(l1)
l2=l1*3

str='ayush'
print(str*3)
print(l2)
print(l2.count(4))
print(l2.count(23))
print(l2.count(34))
# print(l2.count(2,5))
# print(l2.count())

print(l2.index(23))
# print(l2.rindex(23)) - error
print(l2.index(23,3))
print(l2.index(23,-4))
# print(l2.index(34))
print(l2.index(23,4,8))
print(l2.index(23,-4,-1))
# print(l2.index(23,-1,-4))

# update
listUpdate=[2,3,4,54,56,7,7,8]
listUpdate[3]=100
print(listUpdate)

# extend

addList=['apple','kiwi','Mango','banana','orange']
l3 = listUpdate + addList
print(l3)

listUpdate.extend(addList)
print(listUpdate)

l4=[1000,2000,3000]
listUpdate.append(l4)
print(listUpdate)

# remove 
print(listUpdate.pop(2)) #index
print(listUpdate)

listUpdate.remove('kiwi') #element
print(listUpdate)

# listUpdate.remove(100000) - error
# print(listUpdate)

# listUpdate.pop(23) -error
# print(listUpdate)

listUpdate.reverse()
print(listUpdate)

l1 = ['apple','kiwi','Mango','banana','orange']
print(l1)
print(sorted(l1))
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

