# https://docs.python.jp/3/libraly/index.html

# 標準ライブラリ

s = 'fafjeaoifjaofneaiobfaiaofbaobae'

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d) # {'f': 6, 'a': 8, 'j': 2, 'e': 3, 'o': 5, 'i': 3, 'n': 1, 'b': 3}


from collections import defaultdict # Importする必要がある

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d) # defaultdict(<class 'int'>, {'f': 6, 'a': 8, 'j': 2, 'e': 3, 'o': 5, 'i': 3, 'n': 1, 'b': 3})

print(d['a'])
