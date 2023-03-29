'''
1. Take one list from user and print that list. and remove duplicate elements from list.
2. Take two list from user and merge that two list into another list.

    l1=[1,2,3]
    l2=[6,7,8]
    l3=[1,2,3,6,7,8]

3. Take one list from user and return list like this:

    l = [1,2,3,4]
    o/p: [1,4,9,16]
 
    
4. Take one list from user in string. and make one list that contain only lower string element.

    l =['Apple','KIWI','banana','orange']
    o/p: ['banana','orange']

    
5. Print sum of digit in list.

    l = [2423,3534,35643]
    l2=[11,15,21]

6. Input comma separated string convert into list and after that print sum of all element.

string - 1,2,4,5,6

l = [1,2,4,5,6]
sum: 18

'''

# 1. 
l = [1,2,3,4,1,5,6,1,7,2,8]
l2 = []

for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

# 3. 

l=[2,3,4,5]
s=[]

for i in l:
    s.append(i**2)

print(s)

# 4. 

# l=[]
# l2=[]
# for i in range(4):
#     l.append(input("Enter string: "))

# print(l)

# for i in l:
#     if i.islower():
#         l2.append(i)
# print(l2)


# 5. 

l=[]
for i in range(4):
    l.append(int(input("Enter a no:")))
print(l)

l2=[]
for i in l:
    sum=0
    while(i>0):
        rem=i%10
        sum=sum+ rem
        i=i//10
    l2.append(sum)

print(l2)
    
# 6.

str=input("Enter a String: ")
l1 = str.split(',')
print(l1)
l2=[]

sum=0
for i in l1:
    l2.append(int(i))
    sum = sum + int(i)

print(l2)
print(sum)