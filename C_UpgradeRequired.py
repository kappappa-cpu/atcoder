# https://atcoder.jp/contests/abc426/tasks/abc426_c
# C - Upgrade Required

"""
バージョンの情報と台数をリストのインデックスでまとめる

最初:
[1,1,1,1]
->
2以下を3に更新
[1,1,3,1]
"""
import sys

it = iter(map(int, sys.stdin.buffer.read().split()))

N = next(it)
Q = next(it)

seq = [1] * N

# これ以下のインデックスは触る必要がない
m = 0

for i in range(Q):
  ans = 0
  x = next(it) - 1
  y = next(it) - 1
  if m < x:
    ans = sum(seq[m:x+1])
    m = x+1
    seq[y] += ans
  elif m == x:
    m = x+1
    ans = seq[x]
    seq[y] += ans
  print(ans)
  