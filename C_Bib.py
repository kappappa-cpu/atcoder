# C_Bib
# https://atcoder.jp/contests/abc392/tasks/abc392_c
n = int(input())

plist = [int(i) for i in input().split()]
qlist = [int(i) for i in input().split()]

corres = dict()

for p, q in zip(plist,qlist):
  corres[q] = p
  
answer = []

for i in range(n):
  answer.append(str(qlist[corres[i+1]-1]))
  
print(" ".join(answer))
