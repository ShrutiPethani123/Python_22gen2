# recursion: function calling itself

# def printNum(n):
#     # base case
#     if(n==0):
#         return    
#     print(n)
#     printNum(n-1)

# printNum(5)


'''
5! = 5*4*3*2*1 =120
5! = 5 * 4! 
5! = 5 * 4 * 3!
5! = 5 * 4 * 3 * 2!
5! = 5 * 4 * 3 * 2* 1!
5! = 5 * 4 * 3 * 2 * 1
'''

# def fact(n):
#     if(n==1):
#         return 1
#     return n*fact(n-1)

# print(fact(4))


# print 1 to 10 number using recursion.
# fun(10)
# 1 2 3 4 5 6 7 8  9 10

# def printNum(n):
#     if n==0:
#         return
#     printNum(n-1)
#     print(n)

# printNum(10)

# print fibonacci series using recursion.
# 0 1 1 2 3 5 8 13 ....


# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(2))
# print(fib(5))

# for i in range(10):
#     print(fib(i),end=" ")


def fibonacci(n,first,sec):
    if n==0:
        return
    print(first,end=" ")
    fibonacci(n-1,sec,first+sec)


fibonacci(1000,0,1)




