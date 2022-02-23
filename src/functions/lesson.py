### https://docs.python.org/ja/3/library/functions.html

import builtins # インポートすること💚
# Python 組み込み関数
print(globals())

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}
print(ranking.get('A'))
print(sorted(ranking, key=ranking.get, reverse=True))