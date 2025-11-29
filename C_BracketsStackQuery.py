# https://atcoder.jp/contests/abc428/tasks/abc428_c
# C - Brackets Stack Query

'''
(を+1、)を-1とすると、
良い括弧列であれば、
1. 部分和の各要素が0以上
2. 部分和の最後の要素が0
3. あるいは空
であることを利用している

Appendix
()のbracketによる言語をdyck言語というそう
'''

import sys

it = iter(sys.stdin.buffer.read().split())

q = int(next(it))

brackets = []

prefix = []
last = 0
minusCounter = 0

for _ in range(q):
  if int(next(it)) == 1:
    braket = next(it).decode("utf-8")
    if braket == '(':
      brackets.append(1)
      last+=1
    else:
      brackets.append(-1)
      last-=1
    prefix.append(last)
    if last < 0:
      minusCounter+=1
  else:
    poped = brackets.pop()
    last -= poped
    if prefix.pop() < 0:
      minusCounter-=1
  if brackets == [] or (last == 0 and minusCounter == 0):
    print('Yes')
  else:
    print('No')

