# l = [1,2,3,4,5,6]

# l2 = [i for i in l]
# print(l2)

# l2 = [i*2 for i in l]
# print(l2)

# l3 = [i for i in l if i%2==0]
# print(l3)

# print([i for i in l if i>3])

# l2=[i for i in range(1,11)]
# print(l2)

# l= [int(input()) for i in range(4)]
# print(l)

l=['india','china','usa','canada','uk']

# make one list that element length have less than 3
print([i for i in l if len(i)<3])

# Make one list that contain all upper case element
print([i.upper() for i in l])

# Make one list that contain all elements that have 'a' in string
print([i for i in l if 'a' in i])
print([ i for i in l if i.find('a')!=-1])
print([ i for i in l if i.count('a')>0])

# 
b=10
a= f'''
This    is
is
multi
line
comment
{b}
'''
print(a)