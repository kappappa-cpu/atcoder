# https://atcoder.jp/contests/abc408/tasks/abc408_c
# C - Not All Covered

"""
prefixを応用しm*n次元の処理をn次元で処理
"""

import numpy as np

n, m = map(int,input().split())

# 差分配列
# 0がn+1入る
diff = np.zeros(n+1,dtype=int)

# 始点と終点の左隣に+1-1する
for i in range(m):
  l, r = map(int,input().split())
  diff[l-1] += 1
  diff[r] -= 1
  #print(diff)
  
# 累積和を取ることでm*n次元の列ごとの総和が取れる
# 体系化:離散微分、離散積分
print(min(np.cumsum(diff[:-1])))