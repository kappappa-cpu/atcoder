# https://atcoder.jp/contests/abc313/tasks/abc313_b
# B - Who is Saikyo?

import sys
# 再帰制限を解除
sys.setrecursionlimit(10**7)

def dfs(u, graph, seen):
  """
  input:
   u:int invに入っている弱い側
   graph:list 弱い->強いを表している
   seen:list uより強いものが入っているsetを入れる
  """
  for v in graph[u]:
    if v not in seen:
      seen.add(v)
      # さらにvより強いものを探していく
      dfs(v,graph,seen)
  

n, m = map(int,input().split())

# 弱い->強い
inv = [[] for _ in range(n)]

for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  inv[b].append(a)

# 各ノードに親（強い側）が存在するか確認するためのリスト
ancesters = [set() for _ in range(n)]
for i in range(n):
  dfs(i, inv, ancesters[i])

# 自分より強いものがいない（ancesters[i]が空集合）が答えの候補
roots = [i+1 for i in range(n) if not ancesters[i]]

if len(roots) == 1:
  print(roots[0])
else:
  print(-1)