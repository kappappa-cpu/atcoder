# https://atcoder.jp/contests/abc411/tasks/abc411_c
# C - Black Intervals

import itertools

n,q = map(int,input().split())

A = [int(i)-1 for i in input().split()]

masu = [0 for _ in range(n)]

count = 0

if n == 1:
  for i in range(q):
    if i%2 == 0:
      print(1)
    else:
      print(0)
  exit()

for i in range(q):
  if i == 0:
    masu[A[i]] = 1
    count += 1
    print(1)
    continue
  if masu[A[i]] == 1:
    #減らす
    masu[A[i]] = 0
    if A[i] == 0:
      if masu[A[i]+1] == 0:
        count-=1
    elif A[i] == n-1:
      if masu[A[i]-1] == 0:
        count-=1
    elif masu[A[i]-1] == 1 and masu[A[i]+1] == 1:
      count+=1
    else:
      if masu[A[i]-1] == 0 and masu[A[i]+1] == 0:
        count-=1
  else:
    #追加
    masu[A[i]] = 1
    if A[i] == 0:
      if masu[A[i]+1] == 0:
        count+=1
    elif A[i] == n-1:
      if masu[A[i]-1] == 0:
        count+=1
    elif masu[A[i]-1] == 1 and masu[A[i]+1] == 1:
      count-=1
    else:
      if masu[A[i]-1] == 0 and masu[A[i]+1] == 0:
        count+=1
  print(count)