# -*- coding: utf-8 -*-

t = (1, 2, 3, 4, 5, 1, 2)

print(t)

type(t)

print(t[0])
print(t[-1])

print(t[2:5])
print(t.index(1))

print(t.index(1, 1))
print(t.count(1))

t = ([1, 2, 3], [4, 5, 6])

print(t[0][0])

new_tuple = (1, 2, 3) + (2, 3, 4)

print(new_tuple)


## unpacking

num_tuple = (10, 20)
print(new_tuple)

x, y = num_tuple
print(x, y)

min, max = 0, 100
print(min, max)


i = 10
j = 20
tmp = i
i = j 
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
b, a = a, b
print(a, b)

##
chose_from_two = ( 'A', 'B', 'C')

answer = []
answer.append('A')
answer.append('B')
print(chose_from_two)
print(answer)
