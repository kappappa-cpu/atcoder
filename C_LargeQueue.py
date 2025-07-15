# https://atcoder.jp/contests/abc413/tasks/abc413_c
# C - Large Queue

"""
テーマ: queue構造は使わない
dequeのpopleft()をidxを増やし、参照インデックスを変化させることで
リストの先頭削除計算量を回避
"""
q = int(input())

# [[3,2],[4,5]] 3が2個、4が5個
record = []
idx = 0

for i in range(q):
  query = [int(j) for j in input().split()]
  #print("queryは: ",query)

  if query[0] == 1:
    record.append([query[2],query[1]])
  else:
    flag = True
    left = query[1] + 0
    sumation = 0
    while flag:
      #print(record[0][1],left)
      #print("record: ", record)
      if record[idx][1] < left:
        left = left - record[idx][1]
        sumation += record[idx][0] * record[idx][1]
        idx += 1
      elif record[idx][1] == left:
        sumation += record[idx][0] * record[idx][1]
        idx += 1
        flag = False
      elif record[idx][1] > left:
        sumation += record[idx][0] * left
        record[idx][1] -= left
        flag = False
        
    print(sumation)
        
    