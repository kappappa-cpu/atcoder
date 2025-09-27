# C - New Skill Acquired
# https://atcoder.jp/contests/abc424/tasks/abc424_c

import sys
from collections import deque

'''
「データ構造を反転させて」
スキル->前提から前提->スキルの有向グラフを認識する
入力例1だと
(1) ──▶ (2) ⇄ (3)
                 ▲
                 └── self (3→3)
(4) ──▶ (6) ──▶ (5)
 ▲        ▲       │
 │        └───────┘
 └────────────────┘
（6→6 は self ループあり）

'''

# 普通にfor文で入力を取ってくるやり方と...
# sys.stdin.buffer.read().split()を使う方法で比べると...
# 300msほど違いました
it = iter(map(int, sys.stdin.buffer.read().split()))
N = next(it)

# !!!adjの構造が最重要!!!
# この後のfor文を見よ
adj = [[] for _ in range(N+1)]

# i番目のスキルが学習済であればTrue
# 入力に合わせて0番目は不使用データ
learned = [False]*(N+1)

# 習得済みのスキルを保存しておく
# キュー構造を使うことでFIFO（先入れ先出し）を効率的に行う
q = deque()

# a番目またはb番目のスキルがi番目のスキルの前提条件になっていることを保存
for i in range(1, N+1):
  a = next(it)
  b = next(it)
  if a == 0 and b == 0:
    learned[i] = True
    q.append(i)
  else:
    adj[a].append(i)
    adj[b].append(i)

while q:
  # すでに習得済みのスキルを取り出し...
  v = q.popleft()
  # そのスキルが前提となっている未習得のスキルを習得済みにする
  for u in adj[v]:
    if not learned[u]:
      learned[u] = True
      q.append(u)

print(sum(learned))