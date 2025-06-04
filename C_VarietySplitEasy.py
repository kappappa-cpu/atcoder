# https://atcoder.jp/contests/abc397/tasks/abc397_c
# C - Variety Split Easy

"""
プリフィクス/サフィックス走査 (prefix/suffix scan)
"""
n = int(input())

inputList = input().split()

# 種類数を順、逆方向で保存
# [1, 2, 2, 3, ...]
forList = []
backList = []

forSet = set()
backSet = set()

# あらかじめ重複なしの種類数を正順でforList、逆順でinvList
# に入れておく
for i in range(n):
  t = int(inputList[i])
  u = int(inputList[n-i-1])
  forSet.add(t)
  backSet.add(u)
  forList.append(len(forSet))
  backList.append(len(backSet))

answer = 0
  
for i in range(n-1):
  answer = max(forList[i] + backList[n-i-2], answer)
print(answer)