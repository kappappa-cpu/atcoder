# https://atcoder.jp/contests/abc398/tasks/abc398_c
# C - Uniquenes

"""
ハッシュテーブルを使って効率化
"""

n = int(input())

numbers = [int(i) for i in input().split()]

# 持っている数: [何番目にあったか, 何個あったか]
dic = {}

for i in range(n):
  try:
    dic[numbers[i]][1] += 1
  except:
    dic[numbers[i]] = [i, 1]
  
    
temp = 1
ans = -1


for i, j in dic.items():
  if j[1] == 1 and temp < i:
    temp = i
    ans = j[0]
if ans == -1:
  print(ans)
else:
  print(ans+1)
