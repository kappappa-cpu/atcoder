# B_Humidifier2
# https://atcoder.jp/contests/abc383/tasks/abc383_b

"""
numpy.arrayの行列を無理やり使う
"""

import numpy as np

def cal(p,s):
  """
  加湿器を2つ置いたらいくつの床を加湿できるか返す
  Parameters:
    p(tuple):加湿器を置く座標
    s(tuple):同上
  Return:
    int:加湿した床の数
  """
  cor1_mask = (abs(p[0] - rows) + abs(p[1] - cols) <=d)
  cor2_mask = (abs(s[0] - rows) + abs(s[1] - cols) <=d)
  element_mask = (room == ".")
  h = np.sum((cor1_mask & element_mask)|(cor2_mask & element_mask))
  return h

def search():
  """
  加湿器を2つ置く全組み合わせを確認し、加湿可能床数の最大値を返す
  Return:
    int:加湿可能床数最大値
  """
  # 加湿器を置くことができる座標を抽出
  r,c = np.where(room == ".")
  canList = list(zip(r,c))
  sum_ = 0
  for can1 in canList:
    for can2 in canList:
      if can1 == can2:
        continue
      temp = cal(can1,can2)
      if temp > sum_:
        sum_ = temp
  return sum_

h, w, d = map(int, input().split())
# hが高さ
# wが横
# dが加湿器の性能

room = []

for _ in range(h):
  room.append(list(input()))

room = np.array(room)
rows, cols = np.indices(room.shape)

print(search())