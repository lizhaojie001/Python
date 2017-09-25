#_*_ coding utf-8 _*_
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
# initlog()

# Defining Functions
def fib(n):
    a,b = 1,2
    while a<n:
        print str(a) + '\n',
        a,b = b,a+b

fib(200)
'\n'
print fib

# Default Argument Values
# def ask_ok(prompt,retries=4,complaint = 'Yes or no,please'):
#     while True:
#         ok = raw_input(prompt)
#         if ok in ['y','ye','yes']:
#             return True
#         if ok in ('n','no','nop','nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise  IOError('refusenik user')
#         print  complaint
#
# ask_ok('yes',9,"hah")

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

ask_ok('Do you really want to quit?')
i = 5
def f(arg = i):
    print  arg

i = 6
f()
# 4.7.2. Keyword Arguments

def parrot(voltage, state = 'a stiff',action ='voom',type = 'Norwegian blue'):
    print  '__ This parrot woul\'t',action
    print  'if you put ',voltage,'volts through it.'
    print '__ lovely plumage ,the ',type
    print '__ It\'t',state,'!'

parrot(voltage='xx')
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")