'''
1. for
2. while

range:

-> range(end) - 0 to end-1
-> range(start , end) - start to end-1
-> range(start,end,step) - 

'''

# for i in range(5):
#     print("royal",i)


# for i in range(1,5):
#     print(i,end=" ")

# for i in range(6,10):
#     print(i,end=" ")

# for i in range(1,10,2):
#     print(i, end=" ")

# for i in range(10,0,-1):
#     print(i,end=" ")

# No output
# for i in range(10,0):
#     print(i,end=" ")

# for i in range(1,5,-1):
#     print(i,end=" ")

# a=5
# b=10
# i=7
# print("global:",id(i))
# for i in range(a,i+1):
#     print(id(i))
    # print(i,end=" ")

# for i in range(33,73):
#     print(chr(i),end=" ")

# a='45'
# print(type(a))


'''
1. print  50 to 60 number using for loop.
2. print 100 to 10 number using for loop.
3. Take one number from user and print multiplication table of that number.

    3*1=3
    3*2=6
    .
    .
    3*10=30
4. Take one number from user and find factorial of that number.

    5 - 120

5. Take one number from user and check number is prime or not.

6. Find factors of number.

    6 - 1 2 3 6
    15 - 1 3 5 15

7. Take 10 number from user and print that number if number divide by 7 than stop to taking the number. 


'''

# for i in range(1,8):
#     if i==3:
#         # break
#         continue
#     print(i)

# list=["one",'two','three','four']

# for i in list: 
#     if(i=='three'):
#         continue
#     print(i)
# else:
#     print("Completed")


# n=int(input("Enter a no:"))
# flag=True
# for i in range(2,n):
#     if n%i==0:
#         flag=False
#         break

# if flag==True:
#     print(n,"is prime number")
# else:
#     print(n,"is not prime")

for i in range(10):
    n=int(input("Enter a no: "))
    if(n%7==0):
        break
    print(n)
