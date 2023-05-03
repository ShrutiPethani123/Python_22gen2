# map(function , iterator)

def fun1(n):
    return len(n)

result = map(fun1,('canada','india','germany'))
print(list(result))


result = map(fun1,['canada','india','germany'])
print(list(result))

result = map(fun1,{'canada','india','germany'})
print(list(result))

l1=[1,2,3,4,5,6,7,9]
l2=['ram','joy','tom','roy']

def fun2(a,b):
    return b+"@"+str(a)

ans = list(map(fun2 ,l1,l2))
print(ans)


l3=[2,3,4,5,6]
ans = list(map(lambda a: a*a,l3))
print(ans)

# Take two list and them into another list using map.

'''
l1: [1,2,3,4]
l2: [2,3,4,5]
l3:[3,5,7,9]
'''
l1=[1,2,3,4]
l2=[2,3,4,5]

print(list(map(lambda a,b:a+b , l1,l2)))


l=['Apple','mango','orange','kiwi']
# convert all elements into uppercase using map function

l2=list(map(lambda a: a.upper(),l))
print(l2)


