# https://atcoder.jp/contests/abc410/tasks/abc410_c
# C - Rotatable Array

"""
オフセットを持つリングバッファ

       [0]-----[1]
     /             \
   [n]             [2]
   |                 |
   [6]             [3]
     \             /
       [5]-----[4]

"""

from collections import deque

n, q = map(int,input().split())

A = list(range(1,n+1))

offset = 0

for _ in range(q):
  temp = list(map(int,input().split()))
  if temp[0] == 1:
    A[(temp[1]-1 + offset)%n] = temp[2]
  elif temp[0] == 2:
    print(A[(temp[1]-1+offset)%n])
  else:
    offset = (offset + temp[1]) % n