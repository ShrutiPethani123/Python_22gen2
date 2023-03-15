# string is oredered and immutable

'''
s = "java TechnoLOGY is BEST"

print("Length: ",len(s))
print("Capitalize: ",s.capitalize())
print("Upper: ",s.upper())
print("Lower: ",s.lower())
print("Title: ",s.title())
print("Swapcase: ",s.swapcase())

print(s,id(s))
print(s.lower(),id(s.lower()))
s1=s.lower()

'''


# s = 'Python is a Good Programming language. and it is easy language also'

'''
print(s.count('i'))
print(s.count('language'))
print(s.count("z"))
print(s.count(" "))
print(s.count("is",10))
print(s.count("is",10,60))
print(s.count("is",2,-40))
print(s.count("s",-40,-2))
'''

'''
count(string)
count(string,start)
count(string,start,end)

'''
s = 'Python is a Good Programming language. and it is easy language also'

print(s.startswith('P'))
print(s.startswith('Python'))
print(s.startswith('python'))
print(s.startswith('Good',12))
print(s.startswith('Good',12,49))

print(s.endswith('P'))
print(s.endswith('also'))
print(s.endswith('a'))
print(s.endswith('o',3))
print(s.endswith('o',3,67))


'''
startswith(string)
startswith(string,start)
startswith(string , start , end)

endswith(string)
endswith(string,start)
endswith(string , start , end)

'''

s1 = "Good"
s2 = "Morning"

print(s1+s2)
print(s1.__add__(s2))

s1=3
s2=5
print(s1+s2)
print(s1.__add__(s2))

# s1="java"
# s2=45
# print(s1+s2)
# print(s1.__add__(s2))


'''
s = "22General2"

print(s.center(20))
print(s.center(20,'$'))
print(s.center(30,'😊'))
# print(s.center(30,'%%')) - invalid
print(s.ljust(30,'%'))
print(s.rjust(30,'#'))
print(s.rjust(30))

'''
s = "Monday Tuesday Monday "
print(s.find('M'))
print(s.find('day'))
print(s.find('day',5))
print(s.find('day',1,20))
print(s.find('z')) # return -1 if string not present

print(s.index('M'))
print(s.index('Monday'))
print(s.index('day',5,20))
# print(s.index('z')) # give error if string not present

print(s.rfind('day'))
print(s.rfind('day',2,15))
print(s.rfind('f'))

print(s.rindex('day'))
print(s.rindex('day',2,15))
# print(s.rindex('f')) - error

print(s.find('da',12,20))


s = "Java PYTHON"
s1 = "java"
s2 = "PYTHON"
s3= 'Java Python'

print(s.isupper())
print(s1.isupper())
print(s2.isupper())

print(s.islower())
print(s1.islower())
print(s2.islower())

print(s.istitle())
print(s1.istitle())
print(s2.istitle())
print(s3.istitle())


'''
Task: 

1. Take one string from user and print first , last and middle character for only odd length string if user entered even length then print invalid input.

    s - pythons
    o/p - phn

2. 

str = " Good Morning"
o/p= **********Good Morning%%%%%%%%%%%%%%% (only using ljust and rjust)

'''

str = " Good Morning"
s1=str.rjust(22,"*").ljust(37,"%")
print(s1)
