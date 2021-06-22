#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
type(a)

b = {2, 3, 3, 6, 7}

print(a - b)

print(b - a)

print(a & b)

print(a | b)

print(a ^ b)


s = {1, 2, 3, 4, 5}

s.add(6)
s.add(6)
s.add(6)

s.remove(6)

s.clear()

blank_set = set()
print(blank_set)


my_friends = {'A', 'C', 'D'}
A_friends = {'B' ,'D', 'E', 'F'}

print(my_friends & A_friends)

f = {'apple', 'banana', 'apple', 'banana'}
kind = set(f)
print(kind)
