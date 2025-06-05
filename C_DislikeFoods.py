# https://atcoder.jp/contests/abc402/tasks/abc402_c
# C - Dislike Foods

"""
インクリメンタル更新（incremental update）

全探索の計算量をインクリメンタル更新で回避する
"""

n, m = map(int,input().split())

# 辞書{食材:メニューの集合}
menu = {}
# 各料理の食材数を入れる
badCounts = [0] * m
# 食べられる料理の数
goodMCounts = 0

# menu初期化
for i in range(n):
  menu[i+1] = set()

# menuとbadCountsにデータを追加していく
for i in range(m):
  flag=True
  for j in input().split():
    if flag:
      badCounts[i] = int(j)
      flag=False
    else:
      menu[int(j)].add(i+1)

"""
克服したら各料理の食材数badCountをデクリメント
各料理の食材数が0になっている場合はそもそもチェックしないようにする
食材数を減らした後badCountが0になっていたら食べられる料理の数goodMCountsをインクリメント
"""

for kokufuku in input().split():
  for menu_id in menu[int(kokufuku)]:
    if badCounts[menu_id-1] == 0:
      break
    else:
      badCounts[menu_id-1]-=1
    if badCounts[menu_id-1] == 0:
      goodMCounts+=1
  print(goodMCounts)