'''
function: block of code

type:

1. pre define
2. user define

r.t name()
{

}

'''

def display():
    print("Hello...")

display()
display()

def add(a,b):
    return a+b

ans=add(3,4)
print(ans)

print(add(2,9))


'''
1.  Make one function for check number is prime or not.
checkPrime---> True , False

2. Take Two number from user and print all the palidrom number between that range.

100 200


'''

# def checkPrime(n):
#     if(n==1):
#         return None
#     if(n==2):
#         return True
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True

# m= int(input("Enter a no: "))
# if(checkPrime(m)):
#     print("Prime Number")
# elif(checkPrime(m)==None):
#     print("............")
# else:
#     print("Not Prime")


def checkPlaindrom(n):
    temp=n
    rev=0
    while(n!=0):
        rem = n%10
        rev = rev*10 + rem
        n=n//10
    if(temp==rev):
        return True
    return False

def printPalindrom(start,end):
    for i in range(start,end+1):
        # s=str(i)
        # if(s==s[: : -1]):
        #     print(i)
        if(checkPlaindrom(i)):
            print(i)

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
printPalindrom(start,end)






