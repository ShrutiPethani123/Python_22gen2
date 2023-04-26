# d2={

#     10:'Ahm',
#     11:'baroda',
#     12:'Anand',
#     13:'bhuj',
#     14:'rajkot',
#     15:'surat'
# }

# for i in d2:
#     print(i,d2[i])

# for i in d2.keys():
#     print(i)

# for i in d2.values():
#     print(i)

# for i in d2.items():
#     print(i)


# d4=d2.copy()
# print(d4)


royal ={

    's1':{
        'name':'roy',
        'age':21,
        'email':'abc@gmail.com',
        'isMarried':False
    },
    
    's2':{
        'name':'joy',
        'age':25,
        'email':'xyz@gmail.com',
        'isMarried':True
    },
    
    's3':{
        'name':'tom',
        'age':26,
        'email':'abc@gmail.com',
        'isMarried':True
    }
}

print(royal['s1'])


for i in royal:
    print(royal[i] , type(royal[i]))

print(royal['s2']['email'])

'''

d={

    1:100,
    2:200,
    3:45,
    5:67,
    8:20
}

find maximum and minimum values from dictionary.

'''
d={

    1:100,
    2:200,
    3:45,
    5:67,
    8:20
}

print(max(d.values()))
print(min(d.values()))

