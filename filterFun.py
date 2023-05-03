# filter

def fun(a):
    if a>18:
        return True
    else:
        return False
    
l=[12,34,11,5,7,1,8,9,12,34,56]

l2=filter(fun,l)
print(list(l2))

res= filter(lambda a:a%2==0,l)
print(list(res))


y = lambda a:a%2==0
print(y(10))
print(y(5))