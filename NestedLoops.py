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

'''

# 1


# for i in range(4,8):
#     k=i
#     for j in range(1,5):
#         print(k,end=" ")
#         k=k+i
#     print()

for i in range(4,8):
    for j in range(1,5):
        print(i*j,end=" ")
    print()

# 2.

for i in range(1,5):
    for j in range(1,5):

        if i==1 or j==1 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()