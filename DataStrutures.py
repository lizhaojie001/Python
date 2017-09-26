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
print filter(f,range(2,25))

seq = range(1,10,2)
print seq
seq2 = range(5)
def add(x,y):
    return  x+y
print map(add,seq,seq2)

print reduce(add,range(1,5))
def add(x,y):return x+y
def sum(seq):
    return reduce(add,seq,0)
print sum(range(1,11))

#5.1.4 推导list


