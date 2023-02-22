# Nested Loops

# for i in range(1,4):
#     for j in range(2 , 6):
#         print("i",end=" ")
#     print()


# for i in range(1,4):
#     for j in range(2,6):
#         print(i,end=" ")
#     print()


# for i in range(1,4):
#     for j in range(2,6):
#         print(j,end=" ")
#     print()


'''

1. 

4 8 12 16
5 10 15 20
6 12 18 24
7 14 21 28

2.

* * * *
*     *
*     *
* * * *

3. Take range from user and print all the prime number between range. 

start: 3
end: 10

o/p : 3 5 7 

4. Take range from user and print all perfect number between range.

start: 3
end: 10
o/p: 6

6: 1 2 3 6 ( 1+2+3 = 6) -> perfect

6 28 496 - perfect number



5. Take range from user and print all Armstrong number between range.

1- 0 to 9
3 - 153, 370, 371, 407
4 - 1634, 8208, 9474
5 - 54748, 92727, 93084


'''

# 1


# for i in range(4,8):
#     k=i
#     for j in range(1,5):
#         print(k,end=" ")
#         k=k+i
#     print()

# for i in range(4,8):
#     for j in range(1,5):
#         print(i*j,end=" ")
#     print()

# 2.

# for i in range(1,5):
#     for j in range(1,5):

#         if i==1 or j==1 or i==4 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 3.

# start=int(input("Enter starting range: "))
# end=int(input("Enter ending range: "))

# for i in range(start,end+1):
#     flag=1
#     for j in range(2,i):
#         if(i%j==0):
#             flag=0
#             break
    
#     if flag==1:
#         print(i)

# for i in range(start,end+1):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)
    
# 4. 

# start=int(input("Enter starting range: "))
# end=int(input("Enter ending range: "))

# for i in range(start,end+1):
#     sum=0
#     for j in range(1,i):
#         if i%j == 0:
#             sum=sum+j

#     if(i==sum):
#         print(i)


# 5.

start=int(input("Enter starting range: "))
end=int(input("Enter ending range: "))
# 101 to 500 - 153
for i in range(start, end+1):
    length = len(str(i))
    sum=0
    tmp=i
    
    while i!=0: #153 15 1
        rem= i%10 #3 5 1
        sum = sum + rem ** length  # 3^3+5^3 + 1 =153
        i=i//10 #15 1 

    if(tmp==sum):
        print(tmp)
