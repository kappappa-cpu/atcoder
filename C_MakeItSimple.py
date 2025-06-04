# https://atcoder.jp/contests/abc393/tasks/abc393_c
# C - Make it Simple

"""
集合の集合（frozenset of set)を使う
or
タプルの集合（tuple of set)を使う
"""

n, m = map(int,input().split())

eSet = set()

"""
frozensetバージョン

for _ in range(m):
  _Set = set(map(int,input().split()))
  if len(_Set) != 1:
    # 通常のsetは可変（mutable）でハッシュ不可能（unhashable）
    # なのでsetのsetを作れない
    # frozensetは不変（immutable）でハッシュ可能（hassable）
    # なのでfrozensetを持ったsetを作る
    eSet.add(frozenset(_Set))
print(m-len(eSet))
"""

for _ in range(m):
  u, v = map(int,input().split())
  if u == v:
    continue
  elif u > v:
    _tuple = (v,u)
  else:
    _tuple = (u, v)
  eSet.add(_tuple)
print(m-len(eSet))