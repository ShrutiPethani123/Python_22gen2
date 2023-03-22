'''
string:  ' ' or " " - ordered and immutable
list: [] - ordered and mutable
tuple: ()  - ordered and immutable

'''
list = [1,2,3,4,5]
print(list)

print(type(list))

list = ['java','python','c','c++']
print(list)

l3 = [1, 'java',False , 5.6]
print(l3)

# ordered

print(l3[0])
print(l3[2])
# print(l3[6]) - error

print(l3[1:])
print(l3[-1:-3]) # []
print(l3[-1:-3:-1])
print(l3[2:-1])
print(l3[2:-2])

l1 = ['apple','kiwi','Mango','banana','orange']
print(l1)

for i in l1:
    print(i,end=" ")
print()

for i in range(len(l1)):
    print(l1[i],end=" ")
print()

j=0
while j<len(l1):
    print(l1[j],end=" ")
    j+=1
print()

l2=[2,3,4,5,6]

print("Length: ",len(l2))
print("Max: ",max(l2))
print("Min: ",min(l2))
# print("Min: ",min(l3))
print("sort: ",sorted(l2))
print("reverse: ",sorted(l2,reverse=True))

l1 = ['apple','kiwi','Mango','banana','orange', 'Mongoose']
print(l1)

print("length:",len(l1))
print("Max: ",max(l1))
print("Min: ",min(l1))
print("sort: ",sorted(l1))
print("reverse: ",sorted(l1,reverse=True))

# add element

l1.append("grapes")
print(l1)

l1.insert(2,'guava')
print(l1)

l1.insert(9,'abc')
print(l1)

l1.insert(-3,'xyz')
print(l1)

l1.insert(-30,'xyz')
print(l1)


# task 1: Take one list from user and print that list
# size: 5
# 1 3 4 5 6 

n = int(input("Enter a size: "))
l1=[]

for i in range(n):
    # a = int(input("Enter a no: "))
    # l1.append(a)
    l1.append(int(input("Enter a no:")))

print(l1)

# Task 2: Take one list from user and print all even number from list.
#  n - [1 3 5 6 7 4 8]
# [6,4,8]

even=[]
for i in l1:
    if i%2==0:
        even.append(i)

print(even)

# Task 3: Take one list from user and count total number of negative elements.
# n - [ -1,-2,4,5,-7,-3]
# ans: 4



