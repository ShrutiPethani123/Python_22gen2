# lambda: 

def add(n):
    return n+10

print(add(5))


y = lambda n: n+10
print(y(5))

x = lambda a,b:a+b
print(x(2,3))

def fun1(n):
    return lambda a: a**n

x = fun1(3) # x= lambda a: a**3
print(x(2))
print(fun1(3)(2))