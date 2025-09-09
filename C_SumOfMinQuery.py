#https://atcoder.jp/contests/abc420/tasks/abc420_c
#C - Sum of Min Query

'''
総和の差分をとって、1クエリごとのn回の総和処理を回避
'''

n, q = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

mins = [min(i,j) for i, j in zip(A,B)]
sum_ = sum(mins)

for _ in range(q):
  query = input().split()
  x = int(query[1])
  v = int(query[2])
  old = mins[x-1]
  
  if query[0] == 'A':
    A[x-1] = v
  else:
    B[x-1] = v
  new = min(A[x-1],B[x-1])
  mins[x-1] = new
  sum_ += new - old
  print(sum_)
    