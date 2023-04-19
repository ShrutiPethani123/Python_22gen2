# l1 = [1,2,3,[4,5,68,12],5,9,0,5,[10,2,30,4]]

# print(l1)
# print(l1[2])
# print(l1[3])
# print(l1[3][2])
# l1[3].append(50)
# l1[3].insert(3,100)
# print(l1)

# print(l1[-2])
# print(l1[-1])
# # l1[-1].pop(-2)
# l1[-1].remove(30)
# print(l1)

# # for i in l1:
# #     print(i)

# print([i for i in l1])

l2 = [
    [1, 'ram',22],
    [2,'riya',23],
    [3,'joy',21],
    [4,'jiya',20]
]

for i in l2:
    for j in i:
        print(j,end=" ")
    print()

print([j for i in l2 for j in i ])

for i,j,k in l2:
    print(i,j,k)


'''
1. l = [[1,2,3],[4,6,7,8,9,12],[1],[4],[4,6]] find maximum length list
o/p: [4,6,7,8,9,12]

2. Merge this two list like this

l1=['Hello' , 'How']
l2=['joy','are you']

l3=['Hello joy' , 'How are you']

3. find cumulative sum

l= [1,2,3,5,6]
l2=[1,3,6,11,17]

4. 

l=[10,20,10,20,30,40,10,10] -> remove all 10
o/p:[20,20,30.40]

5. Take one list from user and remove all elements that given by user.

l: [3,4,1,6,7,9,12]
range: 3  7 -> [1,9,12]


'''

lst = [[1,2,3],[4,6,7,8,9,12],[1],[4],[4,6]]

# tmp=[]

# for i in lst:
#     if len(tmp)<len(i):
#         tmp=i

# print(tmp)

# l2=[len(i) for i in lst]
# print(l2)
# max1 = max(l2)
# index1 = l2.index(max1)
# print(lst[index1])

# maxlist = max((i) for i in lst)
# print(maxlist)

# l1=['Hello' , 'How']
# l2=['joy','are you']
# l3=[]

# if (len(l1)==len(l2)):

#     for i in range(len(l1)):
#         l3.append(l1[i]+ " " +l2[i])
#     print(l3)

# l3 = [i+j for i in l1 for j in l2]
# print(l3)

# l= [1,2,3,5,6]
# sum = 0
# l2=[]

# for i in l:
#     sum+=i
#     l2.append(sum)

# print(l2)

l=[10,20,10,20,30,40,10,10,20]

# l.sort()
# i=0
# while(i<len(l)):
#     if(l[i] == 10):
#         l.remove(l[i])
#     else:
#         i+=1
# print(l)

# length = len(l)
# i=0
# while(i<length):
#     if(l[i]==10):
#         l.remove(l[i])
#         length = length-1
#         continue
#     i+=1
# print(l)

l=[3,4,1,6,7,9,12]