# str1 = '0123456789'
### index, slice
# print(str1[-1])
# print(str1[:3])
# print(str1[4:3])
# print(str1[-3:])
# print(str1[::4])
# print(str1[2:9:3])
# print(str1[-2:-9:-3])
# print("tinker"[1:4])

### immutability
# name='sAm'
#  name[0]='p'

### build in method
# print('2'+'3')
# print(name.upper())
# print(name.lower())
# print(name.lower)
# print('this is you'.split())
# print('a,b,c'.split(','))
# str1 =" aDa lovelave "
# print(str1.title())
# print(str1.rstrip()+'.')
# print(str1.lstrip()+'.')
# print(str1.lstrip().rstrip()+'.')
# print(str1.strip()+'.')

### print formating
# template = 'a={},b={}'
# print(template.format('q','e'))

# template = 'a={1},b={0}'
# print(template.format('q','e'))

# template = 'a={0},b={0}'
# print(template.format('q','e'))

# template = 'the {q} {b} {f}'
# print(template.format(f='fox',b='brown',q='quick'))

# result = 1/3
# result = 1.0/3
# print('result = {r:5.5f}'.format(r=result))
# print('result = {:8.5f}'.format(result))

# print('={:9f}'.format(1.2897))

# name='Jose'
# import sys
# print('hello, his name is {}'.format(name))
# print(sys.version_info)
# print(f'hello, his name is1 {name}')

### number
# int, floating
# print(0.2+0.1)
# print(4/2) # divide, always floating
# big_number=14_000_000_000
# big_number=100_0
# print(big_number)

### const
# python hasn't const, can set all uppercase

# import this

### viable assign
# x,y,z=0,1,2
# print(z,y,x)
### list
# my_list=[1,2,3]
# print(my_list)
# print(my_list.index(-3))
# print(my_list.count(-3))
# my_list=['str',100,123.3]
# print(len(my_list))
# my_list.insert(2,222)
# my_list.insert(-2,212)
# # del my_list[0]

# my_list.remove(100) # only first

# print(my_list)
# print(my_list[-1])

# my_list[0]=3
# print(my_list)

# my_list.append('appended')
# print(my_list)

# print(my_list.pop())
# print(my_list)

# my_list.pop(0)
# print(my_list)

# my_list=[3,5,2,8,4,6]
# my_list.sort(reverse=True)
# print(my_list)
# print(sorted(my_list))
# print(reversed(my_list))
# print(my_list)
# for item in my_list:
#    print(item)
# my_list.reverse()
# my_list1=my_list
# my_list1[0]=0
# print(my_list)
# my_list1=my_list[:]
# my_list1[0]=0
# print(my_list)

# for value in range(1,5): # 1,2,3,4
#     print(value)
# print(list(range(1,5)))
# print(list(range(1,5,3)))
# print(min(my_list))
# print(max(my_list))
# print(sum(range(1,1_000_000)))
# squares=[value**2 for value in range(1,11)]
# print(squares)



### dictionary
# unsorted
# retrived by key name, can not be sorted
# list, can be retrived by location, can be indexed or sliced
# my_dict={'key1':'value1', 'key2':'value2', 3:   4}
# print(my_dict)
# print(my_dict['key1'])

# my_dict={'k1':123,'k2':[123],'k3':{'k3_1':100}}
# del my_dict['k1']
# print(my_dict)
# print(my_dict['k3']['k3_1'])
# my_dict['k1']=321
# print(my_dict)
# my_dict['k5']='new kv'
# print(my_dict)
# print(my_dict.keys())
# print(type(my_dict.keys())) # 视图对象
# print(my_dict.values())
# print(my_dict.items())
# print(list(my_dict.keys()))
# print(my_dict.get('k11','not found'))
# for key, value in my_dict.items():
#     print(f'key:{key}, value: {value}')

### tuples
# similar to lists, but immutability
# my_tuple=(1,2,3)
# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[0]=3)

# my_tuple=('a','a','c')
# print(my_tuple.count('a'))
# print(my_tuple.index('a'))
# my_tuple=(1)
# print(my_tuple)
### Set
# unorders, unique elements
my_set=set()
my_set.add()
my_set.add(1)
print(my_set)

# my_set=set('hello')
# print(my_set)
# my_set=set([1,2,3])
# print(my_set)

### boolean
# my_boolean=True
# my_boolean=1>2
# my_boolean=1==1
# print(my_boolean)

# car ='crv'
# print(car == 'crv')
# print(car == 'Crv'.lower())
# age=18
# print(age==18)
# print(age<=19)
# print(age<=19 and age>10)

my_list=[1,2,3]
# print(1 in my_list)
# print(1 not in my_list)

if 4 in my_list:
    print('in')
elif 1==2:
    print('not in')
### else final is not required