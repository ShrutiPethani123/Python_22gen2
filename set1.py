'''
set: unordered and mutable

'''

s1={2,1,3,4,5}
print(s1)
print(type(s1))

s2 = {1,3,1,4,1,6,1,7,2,8,9}
print(s2)

s3={1,3.4,2,6.789,"22gen2","Ahm",4566,(45,46,47)}
print(s3)

s4={34,25,16,1789,2,9,60}
print(s4)
print(len(s4))
print(max(s4))
print(min(s4))
print(sum(s4))

for i in s4:
    print(i, end=" ")

print()

print(9 in s4)
print(3 in s4)

s4.add(700)
print(s4)

s4.add('java')
s4.add(4+8j)
print(s4)

s4.add(60)
print(s4)

s4.update(s1)
print(s4)

s4.update([100,200,300])
print(s4)

# s4.update(34) - error
print(s4)

s4.remove('java')
print(s4)

s4.discard(200)
print(s4)


# s4.remove(1000)
s4.discard(1000)

print(s4.pop())

s4.clear()
print(s4)
del s4


