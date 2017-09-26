# -*- coding: utf-8 -*-
# 4.7.4. Unpacking Argument Lists

# args =range(3,6)


 # Lambda Expressions

a = 4
b = 'bbb'
c =b.__add__('hahha')
print c

x = 5
    # //int(raw_input("请输入一个整数:\n")
if x < 0:
    x =0
    print '我等于0'
elif x == 0:
    print 'zero'
elif x == 1:
    print 'single'
else:
    print 'More'

# for

words = ['cat','window','defenstrate']
for w in words:
    print  w,len(w)

for w in  words[:]:
    if len(w) > 6:
        words.insert(0,w)
print words

print range(10)
print range(5,10)
print range(2,10,3)

a = ['Mary','had','a','title','lamb']
for i in  range(len(a)):
    print  i ,a[i]

# break continue else

for n in  range(2,10):
    for x in  range(2,n):
        if  n % x  == 0:
             print(n,'equals',x,'*',n/x)
        break
    else:
        print  n,'is a prime number'
for num in range(2,10):
    if num%2 ==0:
        print 'Found an even number',num
        continue
    print 'Found a number',num

# pass

# while True:
#     pass

class MyEmptyClass:
    pass

def initlog(*args):
    pass

# initlog()

# 4.6 定义函数

print '#####定义函数######'

def lib(n): #注释1
    """注释"""
    a,b = 0,1
    while a < n:
        print a
        a, b = b ,a+b
# lib(200)

print lib
f = lib
print f(100)

print lib(0)

def lib2(n):  #hahah
    """注释3"""
    result = []
    a,b =0,1
    while a< n:
        result.append(a)
        a,b =b ,a+b
    return result

f100 = lib2(100)
print  f100

print lib2.func_name
print  lib2.func_code
print lib2.func_closure
print  lib2.func_defaults
print  lib2.func_doc
print  lib2.func_globals
print  lib2.func_dict
print  lib.__defaults__

#4.7.5 . Lambda

def make_incrementtor(n):
    """Do thing , but document it
        jiushiwo
    """
    return  lambda x:x+n

f= make_incrementtor(20)
print f(2)
print f(8)

pairs = [(1,'one'),(2,'two'),(4,'four'),(3,'three')]
pairs.sort(key=lambda pair:pair[1],reverse=True)

print pairs

lsb = [(1,'one'),(2,'two'),(3,'three'),(4,'four'),]
lsb.sort(key=lambda pair:pair[1],reverse=True)

print lsb

print lambda a,b:a+b

print make_incrementtor.__doc__

#An Informal Introduction to Python

print 'spam eggs'  # single quotes
print 'doesn\'t'
print  """\
        Uage: thingy [Option]
            -h
            -H hostname
        """