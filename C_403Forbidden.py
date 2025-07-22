# https://atcoder.jp/contests/abc403/tasks/abc403_c
# C - 403 Forbidden

n, m, q = map(int, input().split())

# k番目の集合に番号iがあれば、個別の閲覧権限あり
can_view =  [set() for _ in range(m)]
# i番目がTrueであれば、iさんは全閲覧権限を有する
all_view = [False] * n

for i in range(q):
  data = input().split()
  if int(data[0]) == 1:
    x = int(data[1])
    y = int(data[2])
    can_view[y-1].add(x)
    
  elif int(data[0]) == 2:
    x = int(data[1])
    all_view[x-1] = True
  else:
    x = int(data[1])
    y = int(data[2])
    if all_view[x-1] == True:
      print("Yes")
    elif x in can_view[y-1]:
      print("Yes")
    else:
      print("No")