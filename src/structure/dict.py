#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {'x': 10, 'y': 20}

print(d['x'])

d['z'] = 200

d[1] = 100000

d2 = dict(a=10, b=20)
print(d2)

## method
d.keys()
d.values()


d2 = {'x': 1000, 'j': 500}

d.update(d2)
print(d)

d.get('z')
d.get('x')

d.pop('x')
print(d)

del d['y']
print(d)

d.clear()
print(d)

d = {'x': 10, 'y': 20}

if 'x' in d:
    print('Exist')


dcopy = d.copy()
dcopy['x'] = 20000
print(dcopy)

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}

print(fruits['apple'])
