# https://atcoder.jp/contests/abc421/tasks/abc421_c
# C - Alternated

"""
目標の形との"差"をとり、少ない方を出力

目標:
ABAB... or BABA...
現状:
AABA...

k番目のAの位置を抽出し各k番目の差の絶対値の総和を計算する

kyopro_friendsさんによる解説
https://atcoder.jp/contests/abc421/editorial/13730
"""

N = int(input())
S = list(input())

oddSeq = []
evenSeq = []
SSeq = []

for i in range(N*2):
  if i%2==0:
    evenSeq.append(i)
  else:
    oddSeq.append(i)
  if S[i] == "A":
    SSeq.append(i)
    
answer1 = 0
answer2 = 0
    
for i in range(N):
  answer1 += abs(SSeq[i] - evenSeq[i])
  answer2 += abs(SSeq[i] - oddSeq[i])

print(min(answer1,answer2))