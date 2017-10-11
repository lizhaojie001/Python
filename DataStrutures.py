# -*- coding: utf-8 -*-

# More  on list
list = ['211','232']
print list

list.append(['123'])
list.append(list)

list.extend(list)

list.pop(-1)
print list

# 5.1.1. Using Lists as Stacks¶

list.append('oo')
print list
list.pop(1)
print list

# 5.1.1. Using Lists as Stacks¶
from collections import deque
queue = deque(["ERIC","Jhno","Michael"])
queue.append("ME")
queue.append("GRa")
print queue.popleft()
print queue
print queue.pop()
print queue

#实用的编程工具 filter map


def f(x):return x%3 == 0 or  x%5 ==0
print "filter使用: ---刷选"
print filter(f,range(2,25))

seq = range(1,10,2)
print seq
seq2 = range(5)
def add(x,y):
    return  x+y
print "map使用 -- 对应调用函数"
print map(add,seq,seq2)

print  "reduce的使用 -- 循环调用函数"
print reduce(add,range(1,5))
def add(x,y):return x+y
def sum(seq):
    return reduce(add,seq,0)
print sum(range(1,11))

#5.1.4 推导list
squares = []
for x in range(10):
    squares.append(x**2)

print squares

squares = [x**2 for x in range(10)]
print squares

print u'你好，真是一个不错的名字，欢迎来到%s' %  u"法兰城"
print u'你好冒险者，我是穆，请问你是'
name=raw_input(u'请输入姓名:'.encode('utf-8')).decode('gbk')
print u'%s你好，真是一个不错的名字，欢迎来到%s'%(name.encode("utf-8"),u"法兰城")