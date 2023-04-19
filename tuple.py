'''

string:  ' ' or " "  -> orderd and immutable
list: []   -> ordered and mutable
tuple: ()  -> ordered and immutable


'''

t=(1,2,3,4)
print(t)
print(type(t))

t1 = (2,3,5.6,7.88,"java",'python',[3,4,5])
print(t1)

print(t1[2])
# t1[2]=67
# print(t1)

a=("java")
print(a , type(a))

a=(56)
print(a , type(a))

a=("java",)
print(a , type(a))

print("------------------------------------------------")

t1 = (2,3,5.6,7.88,"java",'python',[3,4,5])

print(t1[4])
print(t1[-4])

print(t1[2:6:3])

# list1=[2,3,4,5,76]
# print(list[1:3])
# list1[2]=45

print(t1[-5:-1:-2])


t3 = 1,2,3,4,5,6,"india",'royal',4.77
print(type(t3))
print(t3)


t4=('india', 'canada', 'usa' , 'china','japan')


for i in t4:
    print(i,end=" ")

print()

for i in range(0,len(t4)):
    print(t4[i],end=" ")
print()


str="royal"
print(str*2)

t4=(2,3,4,5)
print(t4*3)

t5=(2,3,4,5,6,7,90,7,5,3,2,54,6,77,)

print(len(t5))
print(max(t5))
print(min(t5))
print(sum(t5))

print(t5.count(7))
print(t5.count(88))

print(t5.index(7))
print(t5.index(5,6,10))


x1=('ayush','meet','cherish','ansh','rohan','harshil')
x2 = (34,56,12,89,45,46,67,89,90)
x4 =(1,2,3)

x3 = tuple(zip(x1,x2,x4))
print(x3)


# unpack


x1=('ayush','meet','cherish','ansh','rohan','harshil')

a,b,c,d,e,f = x1
# a,b,c,d = x1 - error
# a,b,c,d,e,f,t,g,i = x1 - error
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# a , b , *c = x1
# print(a)
# print(b)
# print(c)

# a , *b , c = x1
# print(a)
# print(b)
# print(c)


a , *b , c , d = x1
print(a)
print(b)
print(c)
print(d)

*a , b , c , d = x1
print(a)
print(b)
print(c)
print(d)


t3 = (1,2,4,5,6,7,8,1,0)

l1 = list(t3)
l1.insert(4,9)
t3 = tuple(l1)
print(t3)




'''
x1=('ayush','meet','cherish','ansh','rohan','harshil')

1. Take one name from user and check that name is present in tuple or not if not present than print not 
found if present than print index.

2. t=(2,3,4,5,1,7,2,8)
print reverse this tuple.


3. t=((1,2,3),(4,5,6),(2,6,7,4),(1,6,7,8))
    print sum of all tuples.
    t=(6,15,19,22)



'''
# 1.
# x1=('ayush','meet','cherish','ansh','rohan','harshil')
# name = input("Enter name: ")

# if name in x1:
#     print("Prsent at index: ",x1.index(name))
# else:
#     print("not Found!!")


#2.
t=(2,3,4,5,1,7,2,8)
# print(t[: : -1])

# l2 = list(t)
# l2.reverse()
# t = tuple(l2)
# print(t)

print(tuple(reversed(t)))




t=(1,2,3,4)

t2=tuple(i*2 for i in t)
print(t2)

t3 = tuple(i for i in t if i%2==0)
print(t3)