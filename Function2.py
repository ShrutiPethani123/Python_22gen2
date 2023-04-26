# default argument

def data(name , age , add="ahmedabad"):
    print(name , age , add)

data('raj',23)
data('joy',12,'baroda')

# def data(name , age , add="ahmedabad",id , college): # non-default argument follows default argument
    # print(name , age , add)


# Keyword Argument

def printName(fname , lname , surname):
     print(fname,lname,surname)

printName('joy','abc','smith')
printName(surname='smith', fname='joy',lname='abc')


# Arbitary Argument (*args)

def printMarks(*marks):
     print(marks)

printMarks(1,2,3,4)
printMarks(12,34,15,6,78,9,1,2,3)
printMarks()
printMarks(90)

# keyword Arbitary Argument (**kwargs)


def printData1(**data):
     print(data)
     print(data['fname'],data.get('lname'))

printData1(fname='raj',lname='patel')



# Take Marks from user and print average of class.

def marks(*m):
     return sum(m)/len(m)

print(marks(90,34,21,56))

# take one list from user and return maximum element from that 

def maxNumber(l):
     return max(l)

l=[2,3,1,5,1,67,23,67,89]
print("Max: " , maxNumber(l))



# take one list from user and return new list with unique element

# def removeDuplicate(l):
#     l2=[]
#     for i in l:
#         if i not in l2:
#              l2.append(i)
    
#     return l2

def removeDuplicate(l):
   return list(set(l))
 
lst=[21,1,4,1,5,2,4,5,3,4,5,7]
print(removeDuplicate(lst))


# pass tuple in function and return multiplication of all element

def mul(t):
    ans=1
    for i in t:
          ans*=i
    return ans
          
t=(1,2,3,4,5)
print(mul(t))


# pass tuple in function and return tuple with add 10 in all element
# t=(1,2,34,5)--> (11,12,44,15)

def add(t):
    l = list(t)
    for i in range(len(l)):
        l[i]=l[i]+10
    t=tuple(l)
    return t
          
t=(1,2,3,4,5)
print(add(t))





