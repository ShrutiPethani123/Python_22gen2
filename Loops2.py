'''
while 

initialization
while condition:
    inc/dec

'''

'''
a=1

while a<=5:
    print(a)
    # a++ - invalid
    a+=1
    # a=a+1

a=10

while a>0:
    print(a,end=" ")
    a-=1

print()

a=1
while a<=10:
    print(a,end=" ")
    a+=2
'''

'''
1. Print multiplication table using while loop.

    6 * 1 = 6
    6 * 2 = 12

2. Take one number from user and count digit of that number.

    n - 242314
    digit - 6

3. Take one number from user and print first and last digit.

    n- 46845
    first:4
    last:5

4. Take one number from user print sum of digits.

    n- 58624
    sum=25

5. Take one number from user and print that number in words.

    n - 546

    five four six


    v- 982

    nine eight two

6. check the number is palindrom or not.

    121 , 8998 , 56365 , 1254521 - palindrom
    1156 , 2368 , 4512 - not palindrom

7. check the number is armstrong or not.

153

1^3 + 5^3 + 3 ^ 3 = 153 (armstrong )

1634

1^4 + 6^4 + 3^4 + 4^4 = 1634 (armstrong )

2**4 (2^4)

8. check the number is perfect number or not .

    6 - 1 2 3 6 ( 1 + 2 + 3 = 6) -> perfect number
    12 - 1 2 3 4 6 12 ( 1+2+3+4+6 = 16) -> not perfect
    28 - 1 2 4 7 14 28 -> perfect number

9. Take two number from user and find hcf/gcd of that number.

    12 -> 1 2 3 4 6 12
    6 -> 1 2 3 6

    gcd : 6

    3
    4

    gcd:1

10. Take two number from user and find LCM of that two number.

    6 - 6 12 18 24 
    12 - 12 24 36

    lcm: 12

    3 - 3 6 9 12 15
    4 - 4 8 12 16

    lcm : 12

    



'''

# n= int(input("Enter a no:"))

# i=1
# while(i<=10):
#     print(f"{n} * {i} = {n*i}")
#     i+=1


# n= int(input("Enter a no:"))
# count=0

# while (n>0):
#     n=n//10
#     count+=1
# print("Total digits: ",count)

# n= int(input("Enter a no:"))

# last=n%10
# a=n

# while n>9: #4567 456 45 4 
#     n=n//10 # 456 45 4
# first=n

# while n>0:
#     rem=n%10
#     n=n//10
# first=rem

# count=0
# while (n>0):
#     n=n//10
#     count+=1
# print("Total digits: ",count)

# p=10**(count-1)
# first=a//p

# print("First digit: ",first)
# print('Last digit:',last)

'''
1357

1357//1000 = 1

'''

# n = int(input('Enter a no: '))

# rev=0

# while n>0: # 735 73 7 0 
#     rem=n%10 # 5 3 7
#     rev=rev*10+rem # 5 53 537
#     n=n//10 # 73 7 0

# print(rev)

# while rev>0:

#     rem=rev%10

#     if rem==1:
#         print('one',end=" ")
#     elif rem==2:
#         print('two',end=" ")
#     elif rem==3:
#         print('three',end=" ")
#     elif rem==4:
#         print('four',end=" ")
#     elif rem==5:
#         print('five',end=" ")

#     rev=rev//10


'''

645

sum=6+4

'''

# print(2**3)
# print(pow(2,3))

# Armstrong number

'''
n=int(input("Enter a no: "))

length = len(str(n))
print(length)
sum=0

temp=n

while temp!=0:
    rem=temp%10
    # sum = sum + (rem ** length)
    sum = sum + pow(rem,length)
    temp=temp//10


if sum==n: 
    print("Armstrong!!")
else:
    print("Not Armstrong")

'''

# a=int(input("Enter a no: "))
# b=int(input("Enter a no: "))

# if a<b:
#     min=a
# else:
#     min=b

# gcd=1

# for i in range(1,min+1):
#     if  a%i==0 and b%i==0:
#         gcd=i

# print(f"GCD of {a} and {b} is {gcd}")

# LCM

a=int(input("Enter a no: "))
b=int(input("Enter a no: "))
count=0

if a>b:
    max=a
else:
    max=b

i=max

while True:
    if i%a==0 and i%b==0:
        lcm=i
        break
    i+=max
    count=count+1

print(f"LCM of {a} and {b} is {lcm}")
print(count)



