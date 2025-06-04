# C_ShortestDuplicateSubarray
# https://atcoder.jp/contests/abc395/tasks/abc395_c

"""
ハッシュテーブルを使って効率化
"""

N = int(input())

A = tuple([int(i) for i in input().split()])

if len(A) - len(set(A)) <= 0 or len(A) == 1:
  print(-1)
  exit()

checkDic = {}
# key:番号, value:[出現回数,前回の座標]

nears = []

for i in range(N):
  a = A[i]
  if a in checkDic:
    checkDic[a][0] += 1
    nears.append(i - checkDic[a][1])
    checkDic[a][1] = i #現在の座標に更新
  else:
    checkDic[a] = [1,i]

print(min(nears)+1)
