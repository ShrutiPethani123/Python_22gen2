'''
1. Arithmetic Operator (+ - / * %  // **)
2. Relational Operator (< > <= >= == !=)
3. Logical Operator (and, or , not)
4. Assignment Operator ( = += -= *= /= &= |=....)
5. Bitwise Operator (& ,| , ^ , ~ , >> , <<)
6. Membership Operator ( in , not in)
7. Identity Operator ( is , is not)


'''

'''
1. Arithmetic Operator (+ - / * %  // **)
''' 
# a=float(input("Enter a no: "))
# b=float(input("Enter a no: "))

# # print("Addition of", a , "and",b , 'is',a+b)
# # print(f"Addition of {a} and {b} is {a+b}")
# print("Addition of {} and {} is {}".format(a,b,a+b))
# print("Substraction of {} and {} is {}".format(a,b,a-b))
# print("Multiplication of {} and {} is {}".format(a,b,a*b))
# print("Division of {} and {} is {}".format(a,b,a/b))
# print("Floor Division of {} and {} is {}".format(a,b,a//b)) 
# print("Exponent of {} and {} is {}".format(a,b,a**b))

'''
floor(1.45) - 1
ceil(1.45) - 2

floor(-2.45) -> -3
ceil(-2.45) -> -2

'''

'''
2. Relational Operator (< > <= >= == !=)

'''

# a=float(input("Enter a no: "))
# b=float(input("Enter a no: "))

# print(a==b)

'''
3. Logical Operator (and, or , not)


and - At signup time Username and password must be right.

T - True
F - False

A   B    A and B

F   F   F
F   T   F
T   F   F
T   T   T

or - 

A   B    A or B

F   F   F
F   T   T
T   F   T
T   T   T

not -

A   not A

T   F
F   T

'''
# a=float(input("Enter a no: "))
# b=float(input("Enter a no: "))
# c=float(input("Enter a no: "))

# print(a>b and b>c)
# print(a>b or b>c)

# # a=4 b=67 c=23
# print(not (a>b or c>a))


'''
4. Assignment Operator ( = += -= *= /= &= |=....) - shorthand notation

++ , --   :- are not in python 

a+=1
a-=1

a=a+b -> a+=b
a=a*b -> a*=b
a=a/b -> a/=b

'''
# a=4
# # a=a+4
# a+=4
# print(a)

'''
5. Bitwise Operator (& ,| , ^ , ~ , >> , <<)

&

A   B   A&B

0   0   0
0   1   0
1   0   0
1   1   1

-> Decimal to Binary 

    15 - 1111
    18 - 0001 0010
    19 - 0001 0011
    178 - 1011 0010
    555 - 0010 0010 1011


-> Binary to Decimal

    1101 
    8+4+0+1 = 13

    ...512    256      128    64    32    16      8    4    2    1

    1101 -> 13
    1100 -> 12
    0011 -> 3
    0011 0010 -> 50
    0001 1100 -> 28
    0111 1001 -> 121


30 -> 0001 1110
      &&&& &&&&  
25 -> 0001 1001
-------------------
      0001 1000 (24)



|


A   B   A|B

0   0   0
0   1   1
1   0   1
1   1   1


30 -> 0001 1110
      |||| |||| 
25 -> 0001 1001
-------------------
      0001 1111 (31)



30 ->    0001 1110 (30)
30<<1 -> 0011 1100 (60) 
30<<2 -> 0111 1000 (120)

n<<m -> n*2^m

30 - >    0001 1110 (30)
30>>1 ->  0000 1111 (15)
30>>2 ->  0000 0111 (7)
30>>3 ->  0000 0011 (3)
30>>4 ->  0000 0001 (1)

n>>m -> n//(2^m)

'''

# print(30&25)
# print(30|25)
# print(30<<1)
# print(30<<2)
# print(30<<10)
# print(30>>1)
# print(30>>4)
# print(30>>50)
# print(-30 | 15)

'''
6. Membership Operator (in , not in)

'''
# l1 = [24,2,6,3,7,8,7]
# print(4 in l1)
# print(7 in l1)
# print(7 not in l1)

'''
7. Identity Operator (is , not is)
'''

list1 = [1,2,3,4]
list2=[10,20,30,40]
list3=[11,22,33,44]

print("list1: ",id(list1))
print("list2: ",id(list2))
print("list3: ",id(list3))

list1=list3

print("----------------------------")
print("list1: ",id(list1))
print("list2: ",id(list2))
print("list3: ",id(list3))

print(list1 is list2)
print(list1 is not list2)

print(list1 is list3)
print(list1)

