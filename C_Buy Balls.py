# https://atcoder.jp/contests/abc396/tasks/abc396_c

import numpy as np

"""テスト用
inputs = iter(["4 3", "5 -10 -2 -5", "8 1 4"])


input = lambda prompt="": next(inputs)
"""

n,m = map(int,input().split())

blist = [int(i) for i in input().split()]
wlist = [int(i) for i in input().split()]

ba = np.array(blist)
wa = np.array(wlist)

# numpyのmaskで当てはまるもののみのsumを取る
maskb_0 = (ba >= 0)
maskw_0 = (wa >= 0)
bnIn0 = np.sum(maskb_0)
wnIn0 = np.sum(maskw_0)

maskb = (ba > 0)
maskw = (wa > 0)
bnNot0 = np.sum(maskb)
wnNot0 = np.sum(maskw)

# 0以上の数で条件を満たしている場合
if bnIn0 >= wnIn0:
  print(ba[maskb_0].sum() + wa[maskw_0].sum())

# Whiteの0を取り除き条件を満たしている場合
elif bnIn0 >= wnNot0:
  print(ba[maskb_0].sum() + wa[maskw].sum())

# 最大の組み合わせを見つける
# baのサイズごとにwaのサイズを調整して条件に合うようにする
else:
  init = 0
  ba_sort = np.sort(ba)[::-1]
  wa_sort = np.sort(wa)[::-1]
  # cumsumの利用により動的計画法的なリソースの節約を試みる
  ba_cumsum = np.cumsum(ba_sort)
  wa_cumsum = np.cumsum(wa_sort)
  for i in range(1,n+1):
    sum_b = ba_cumsum[i-1]
    k = min(i,m)
    sum_w = wa_cumsum[k-1]
    init = max(init,sum_b+sum_w)
  print(init)