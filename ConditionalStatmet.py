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

# if a>0:
#     if a>50:
#         print("Greater than 50")
#     else:
#         print("Less than 50 and positive")
#     # print("Positive")
# elif a==0:
#     print("Zero")
# else:
#     print("Negative")

# print("Thank You!!")

# shorthand notation for if

# if a>5 : print("Hello");print("Good Morning!!")
# else: print(">>>>>")

# # 

# print("Greater than 5") if a>5 else print("Less than 5");print("Thank You")

'''
1. Take one number from user and check number is odd or even.
2. Take one number from user in float and check number is positive , negative or zero.
3. Take two number from user and find minimum number of them.
4. Take Three number form user and find Maximum number.
5. check the candidate is eligible for vote or not. 
6. Take cost price and selling price from user and find profit or loss.

    cp - 100
    sp - 500

    profit - 400

7. Take one character from user and check character is vowel or consonant.

8. Take one number from user and print week days according to that number.
    1 - Sunday
    2 - Monday
    .
    .
    7 - Satuarday
    
    other input: Invalid 

9. Write  a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer, 
    calculate percentage and grade according to given conditions:

	If percentage >= 90% : Grade A
	If percentage >= 80% : Grade B
	If percentage >= 70% : Grade C
	If percentage >= 60% : Grade D
	If percentage >= 40% : Grade E
	If percentage < 40% : Grade F


10. Take rupees from user and count total number of notes.

n= 1593

2000 - 0
500  - 3
100 - 0
50 - 1
20 - 2
10 - 0
5 - 0
1 - 3

11. Write a program to take input from user in seconds and convert into hours and minutes.

	10000 - 2 :46 : 40

12. Write a program to accept the cost price of car display the road tax to be paid 
    according to the following criteria:

    cost price (in Rs)       Tax
    >100000                  15%
    >50000and <=100000       10%
    <=50000                   5% 

    print total amount need to paid.


'''

n=int(input("Enter rs: "))

n2000=n//2000
# n=n%2000
n = n - n2000*2000
n500=n//500
n=n%500

print("2000->",n2000)
print("500->",n500)