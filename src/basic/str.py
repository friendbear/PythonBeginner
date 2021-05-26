#!/usr/bin/env python
# -*- coding: utf-8 -*-


print("I don't know")
print('I don\'t know')

print('hello.\nHow are you?')

print(r'C:\name\name')  # raw

print("#############################")
print("""\
line1
line2
line3\
""")


print("#############################")

s = ('Py                   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'thonssssssssssssssssssssssssssssssssssssssssssssssss')

print(s)

## 文字列のインデックスとスライス
word = 'python'
print(word[0])
print(word[1])
print(word[-1])


print(word[0:2])


print("#############################")
print(word[2:5])
print(word[:5])
print(word[2:])

word = 'j' + word[1:]
print(word[:])

print(len(word))

## 文字のメソッド
s2 = 'My name is Mike. Hi Mike.'
print(s2)
is_start = s2.startswith("My")
print(is_start)
is_start = s2.startswith('X')

print("#############################")

print(s2.find('Mike'))
print(s2.rfind('Mike'))
print(s2.count('Mike'))
print(s2.capitalize())
print(s2.title())
print(s2.upper())
print(s2.lower())
print(s2.replace('Mike', 'Nancy'))
