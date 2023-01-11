'''
Condtional Statment:

1. if else
2. loop


-> 
simple if
if else
nested if
else if ladder

'''

a=int(input("Enter a no: "))

if (a>0):
    if a>50:
        print("Greater than 50")
    else:
        print("Less than 50 and positive")
    # print("Positive")
elif a==0:
    print("Zero")
else:
    print("Negative")

print("Thank You!!")