'''
while 

initialization
while condition:
    inc/dec

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

n= int(input("Enter a no:"))

last=n%10
a=n

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

n = int(input('Enter a no: '))

rev=0

while n>0: # 735 73 7 0 
    rem=n%10 # 5 3 7
    rev=rev*10+rem # 5 53 537
    n=n//10 # 73 7 0

# print(rev)

while rev>0:

    rem=rev%10

    if rem==1:
        print('one',end=" ")
    elif rem==2:
        print('two',end=" ")
    elif rem==3:
        print('three',end=" ")
    elif rem==4:
        print('four',end=" ")
    elif rem==5:
        print('five',end=" ")

    rev=rev//10


'''

645

sum=6+4

'''