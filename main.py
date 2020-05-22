# radius=4
# pi=3.14

# perimeter=2*pi*radius
# print(perimeter)

# area=pi*(radius**2)
# print(area)

# a='hello'
# print(len(a))

# b='hello cold!'
# b[:6]+'g'+b[7:]
# print(b)

# print('hello', end=' - ')
# print('world')

# print("hello", "world")
# print("python", 3.6)

# print("hello", "python", "developers", sep='_')

# a=input()

# age=int(input('Enter your age:'))

# a=float(input())



# conditional statements

# age=float(input())

# if 12<age<18:
#     growth_stage='Teen'
#     print("Growth_stage: " + growth_stage)
# # age=int(age)
# elif 18<=age<21:
#     print("Growth_stage: Young Adult")
# elif age>=21:
#     pass
# else:
#     print("Growth_stage: Child")    
    
    
# print(str(age)+ " years old")



# Loops and lists

# n=int(input())
# i=1
# while i<n:
#     print(str(i),end=' ')
#     i=i+1
# print(i)

# a='hello cold!'
# list(a)

# list(range(10))

# list(range(5, 10))

# list(range(10, 35, 5))

# list(range(30, 10, -2))



# 'green' in ['red', 'blue', 'green', 'orange']

# 'g' in 'green'

# 'green' not in ['red', 'blue', 'green', 'orange']  

# 10 not in range(5, 10)


def add(a, b):
    return a + b
    
print(add(2, 3))


# positional arguments follows keyword arguments(we must first pass positional arg's but not keyword arg's)

def greet(name='world', greeting='hello'):
    print(greeting+' '+name+'!')
    
#function calls

greet()
greet("developers", greeting='hi') 
greet("developers")

#assigning functions to variables

hello=greet

hello()
hello("developers", greeting='hi') 

#passing fucntions as arguments


def Add(a, b):
    return a+b
    
def multiply(a, b):
    return a*b  

def operate(a, b, operation=Add):
    return operation(a, b)      
    
operate(2, 4)

operate(2, 4, operation=multiply)


# lambda functions

add = lambda x, y : x + y     #(    def add(x, y):     return x+y  )

double = lambda x: 2*x

(lambda x, y, z=3: x+y+z)(1,y=2)


'-'.join(['home', 'news', 'abt us', 'events'])
  




def append(a, l=None):
    if l==None:
        l=[]
    l.append(a)
    return l
    


first_ten_even_numbers=[item*2 for item in range(0, 10)]

[int(i) for i in input().split()]  

pairs=[cap+small for cap in ['A','B','C'] for small in ['a','b','c']]


even_numbers=[i for i in range(0,10) if i%2==0]

def mul(*args):
    result=1
    for x in args:
        result *= x
    return result    
    

data=('people', 'hi')

greet(*data)





