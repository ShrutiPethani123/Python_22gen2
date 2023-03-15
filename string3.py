str = "India is best country and India is good Country"
# print(str.split()) # return list
# print(str.split('i')) #['Ind' , 'a ' , 's best country']
# l1=str.split('is')
# print(l1)
# print(str.split('o'))
# print(str.split('o',2))
# print(str.split('o',1))
# print(str.split('o',0))
# print(str.split('z',1))

# print(str.partition('i')) #return tuple
# print(str.partition('is'))
# print(str.rpartition('is'))
# print(str.rpartition('C'))

# print(str.rsplit('a'))
# print(str.rsplit('a',2))

# str = "_a" - True
# str='__' - True
# str="123abc" - False
# str='&abc' - False
# str=" ab cd" - False
# str="class" - True
# str="id" - True
# str='def'
# print(str.isidentifier())

# l3 = str.split('i')
# print(l3)

# s = '-'.join(l3)
# print(s)

# s = 'i'.join(l3)
# print(s)

# s1 = '22gen1'
# print(s1.zfill(9))
# print(s1.zfill(7))
# print(s1.zfill(4))


# dd = input("Enter date(DD): ")
# mm = input("Enter Month(mm): ")

# print(f"{dd.zfill(2)}/{mm.zfill(2)}/2023")


# s1="abcd1234"
# s2 = "abfhjfvdsj"
# s3="dskjf&*^&*^21421"
# s4="352353245"

# print(s1.isalnum()) # True
# print(s2.isalnum()) #True
# print(s3.isalnum()) #False
# print(s4.isalnum()) #True

# print(s1.isalpha())
# print(s2.isalpha()) #True
# print(s3.isalpha())
# print(s4.isalpha())


s1 = "9876543210"
s2 = "5⁴"
s3 = "②⓪②②"
s4 = "½"
s5 = "二千二十二"

# print(s1.isdigit()) # True
# print(s2.isdigit()) # True
# print(s3.isdigit()) # True
# print(s4.isdigit())
# print(s5.isdigit())

# print(s1.isnumeric()) #True
# print(s2.isnumeric()) #True
# print(s3.isnumeric()) #True
# print(s4.isnumeric()) #True
# print(s5.isnumeric()) #True

# print(s1.isdecimal()) #True
# print(s2.isdecimal())
# print(s3.isdecimal())
# print(s4.isdecimal())
# print(s5.isdecimal())




'''
1. Take one string from user and print middle 3 character if string length is odd.

s - 'Python' -> even length -> invalid input
s - India -> ndi
s - Malyalam1  -> yal

India
01234

len-1/2 = 5-1/2 = 2


2. Take one string from user and convert into uppercse if string contain minimum two uppercase in first four letter.

s - PYthon
o/p: PYTHON

s - pYTHon
o/p: PYTHON

s- pythON
o/p: pythON


3. Take one string from user and print sum of all digits.

s - abdgh4213
o/p: 10

s - 354gyjdgs%$%$*55
o/p: 22




'''
# 1.
# s = input("Enter a string: ")
# print(s)

# if len(s)%2==0:
#     print("Invalid Input!!")
# else:
#     m = (len(s))//2
#     print(s[m])
#     print(s[m-1:m+2])



# 2.
# # s =input("Enter a string: ")

# # count=0
# # for i in range(0,4):
# #     if s[i].isupper():
# #         count+=1

# # if count>=2:
# #     print(s.upper())
# # else:
#     print(s)


# 3.
str = input("Enter a string: ")
sum=0
# for i in str:
#     if i.isdigit():
#         sum=sum+int(i)

for i in range(0,len(str)):
    if str[i].isdigit():
        sum=sum+int(str[i])
print(sum)






