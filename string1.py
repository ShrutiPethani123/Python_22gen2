str = "Python"
print(str)

str='java'
print(str)

print(type(str)) #<class 'str'>

s = "Good Morning"
#    0123456789 10 11
#    -12 -11 -10 .... -1

# print(s[0])
# print(s[4])
# print(s[9])
# # print(s[12]) # error  - string index out of range

print(s[-2])
print(s[-3])


# slicing
'''
[start:end] - start to end-1
[start: ] - start to length of string
[: end] - s[0] to s[end-1]
[:] - full string
[start:end:step]

'''

s = "Good Morning"
#    0123456789 10 11
#    -12 -11 -10 .... -1

print(s[1:3])
print(s[2:9])
print(s[3:])
print(s[:7])
print(s[:])
print(s[2:8:2])
print(s[1:9:3]) # 1 4 7
print(s[3:11:4]) # 3 7 
print(s[10:2:-1])
print(s[5:8:-1])  # print - nothing why ? - start<end
print(s[-2:-5])
print(s[-5:-2])
print(s[-2:-5:-1])
print(s[: : -1])

rev = s[: : -1]
print(rev)

print(s[2:-4])
# print(s[2:-4:-1])