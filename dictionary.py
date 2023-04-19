'''
{
    key:value,
    key:value
}


'''

d={
    'a':'apple',
    'b':'banana',
    'k':'kiwi',
    'm':'mango',
    'a':'abc'

}

print(d)
print(d['k'])
print(d['m'])


d1={
    'name':'raj',
    'age':22,
    'email':'raj@gmail.com',
    'hobbies':['reading','swimming']
}

print(d1['name'])
print(d1['hobbies'])
print(d1['hobbies'][0])

print(len(d1))
print(type(d1))

d3 = dict(name='joy',age=21,contactno=3514634166)
print(d3)

# access the value of dict

print(d1['age'])
print(d1.get('age'))

# print(d1["name2"])
print(d1.get('name2'))

d2={
    'name':'raj',
    'age':22,
    'email':'raj@gmail.com',
    'hobbies':['reading','swimming'],
    None:"java"

}

print(d2)
print(d2[None])

print(d2.keys())
print(d2.values())
print(d2.items())

# update

d2['name']='meet'
print(d2)

d2.update({'name':'ansh',"email": 'xyz@190.com'})
print(d2)

d2['contact']=3532067046
print(d2)

d2.update({'isActive':True})
print(d2)

print(d2.pop('name'))
print(d2)

d2.popitem()
d2.popitem()
print(d2)


# d2.clear()
# print(d2)

# del d2
del d2['age']
print(d2)
