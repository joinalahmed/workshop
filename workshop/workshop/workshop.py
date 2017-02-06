# Just printing hello world

# Note that print	is a function
print('hello world') 

# Numbers
# Two kind of numbers : 
print(52.3E-4)
print(2 + 2) 
print(2.0 + 2)

# Division
print(1.0 / 2)
print(1.0 // 2)

# Mod
print(5 % 2)

#power 
print(2 ** 5)

#Variables 
# Just like other languages
x = 3
print(x * 2)

# input 
#y = input("y : ")
#print(y)
#print(pow(6,8))

# some usefull command : 
print(abs(-10))
print(round(0.75))

# modules 

# Math!
import math
from math import tan
from math import tan as tangent

print(math.tan(45))
print(tan(45))
print(tangent(45))
print(math.floor(65.5))

from math import ceil
print(ceil(32.6))

from math import sqrt
print(sqrt(36))

# Cmath 
import cmath
print(cmath.sqrt(-1))
print((5+1j)*(2+6j))

# strings
print("Let's go")
print('"Hello" she said')
print("\"Hello\" she said")

# Join strings
A = "Hello, "
B = "world"
C = 2017
print(A + B + " " + str(C))

# print long strings 
print('''it is a 
very long string ''')

# row string 
print(r'C\programs\s.py')

# data structures
# x(0) x(1) x(2)   x(-2) x(-1)
# List & tuples
l1 = ['saeed', 5]
l2 = [l1 , '3']

# common methods in data 
A = 'Hello'
print(A[0])
print(A[-1])

print(A[2:4])
print(A[2:])
print(A[:])


B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(B[0:5:2])
print(B[::-1])

# len 
# min
# max
# del 
# list.append
# list.count
# list.extend
# list.index('saeed')
# list.insert(3,'s')
# list.pop() != list.append
# list.remove
# list.reverse
# list.sort()
# y = sorted(x)
# cmp(x,y)

#tuple

x = tuple([1,2,3]);
print(x)

y = tuple('abc')







