
### input
# message=input('please input sth:')
# print(message)
# print(type(message))
# print(message>21)
# print(int(message)>21)

### while
# count = 0
# while count<=10:
#     count+=1
#     if count %2==0:
#         continue
#     if count >6:
#         break
    
#     print(count)

### function
def greet_user():
    print('hello!')
# greet_user()

def greet_user(name):
    print(f'hello {name}')
# greet_user('ada')

## location argument
def greet_user(name, age):
    print(f'hello {name}, age: {age}')

# greet_user('ada',12)

## keyword argument

# greet_user(age=12,name='tom')

## default value
def greet_user(name, age=3):
    print(f'hello {name}, age: {age}')
# greet_user(name='tom')
# greet_user('tom')

## return value
def get_name(first_name, last_name):
    full_name=f'{first_name} {last_name}'
    return full_name.title()

# print(get_name('linda', 'marid'))

## multi param
# def make_pizza(size, *toppings):
#     print(size)
#     print(toppings)
# make_pizza(12,'a','b','c') # ('a', 'b') tuple

## import
# import pizza
# pizza.make_pizza(12,'a','b','c')

# from pizza import make_pizza
# make_pizza(12,'a','b','c')

# from pizza import make_pizza as mp
# mp(12,'a','b','c')

# import pizza as p
# p.make_pizza(12,'a','b','c')

# from pizza import *
# make_pizza(12,'a','b','c') # override

### class
from dog import *

# my_dog=Dog('kit',6)
my_dog=Dog()
# my_dog.name='dogge'
# # print(my_dog.name)
# my_dog.roll_over()
my_dog.sit()

# black_dog=BlackDog('bob',9)
# black_dog.roll_over()
# black_dog.sit()

### python stand lib
from random import randint,choice
# print(randint(1,6))
players=[1,2,3,4,5,6]
print(choice(players))