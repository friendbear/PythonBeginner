#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = [1,  0, 4, 50, 2, 1, 2]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])

a = ['a', 'b', 'c']
n = [1 , 2, 3]
x = [a, n]
print(x)

print(x[1])
print(x[1][0])


## Operation
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[0] = 'X'
print(s[0])

print(s[2:5])

s[2:5] = []
print(s[:])
s[:] = []
print(s)  # Empty List

##########
n = [1, 2, 3, 4, 5, 6, 7, 8, 0 ,10]

n.append(100)
print(n)

n.insert(0, 200)
print(n)

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)


s = 'My name is Mike.'
to_split = s.split(' ')
x = ' ######'.join(to_split)
print(x)

## List Copy
i = [1, 2, 3, 4, 5]
j = i  # reference
j[0] = 100
print('i = ', i)
print('j = ', j)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x = ', x)
print('y = ', y)


X = [ 'a', 'b']

###
seat = []
min = 0
max = 5
min <= len(seat) < max
seat.append('p')
seat.pop(0)
print(seat)
