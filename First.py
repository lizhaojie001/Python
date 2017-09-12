# First Steps Towards Programming
# print u'Hello world'
#
# a, b= 0, 1
# while b < 10000:
#     print('b='+str(b))
#     a, b = b, a + b
#     print 'a='+str(a)+'\n'
#
# i = 256*256
# print('the value of i is ',i)
#
# print -2**3

# More Control Flow Tools!!!
# x = int(raw_input("pleas enter an integer:"))
# if x<0:
#     x = 0
#     print 'Negative changed to zero'
# elif x==0:
#     print  'Zero'
# else:
#     print  'More'

# for Statements
words =['cat','window','defenestrate']
for w in  words:
    print  w, len(w)

print  words
for w in  words[:]:
    if len(w)>6:
        words.insert(0,w)
print  words

# The range() Function
a = range(10)
print  a

a = range(5,20)
print  a

a= range(0,10,4)
print  a

a = range(-10,-100,-30)
print a

a = ['mary','bad','a','little','lamb']
for i in range(len(a)):
    print  i,a[i]
for n in  range(2,10):
    for x in  range(2,n):
        if n%x == 0:
            print n,'equals',x,"*",n/x
            break
    else:
        print n,'is a prome number'
# pass Statements

# while True:
#     pass
def initlog(*args):
    pass
initlog()

# Defining Functions
