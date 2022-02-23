# https://docs.python.jp/3/libraly/index.html

# 標準ライブラリ

s = 'fafjeaoifjaofneaiobfaiaofbaobae'

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)
