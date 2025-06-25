# https://atcoder.jp/contests/abc387/tasks/abc387_c
# C - Snake Numbers

"""
「ワープと桁上り」
最上位桁とnの桁を確認していき、同じか大きい場合はn+1桁を桁上りしてチェックしていく
nの桁より下が0のみだったら最上位桁のdigit乗でワープをする
"""

def findDigit(number) -> int:
  """
  桁数を返す
  """
  k = 0
  while 10**k <= number:
      k += 1
  return max(k, 1)

def findTopNumber(number) -> int:
  """
  最上位桁の数字を返す
  """
  return number//10**(findDigit(number)-1)

def findCertainNumber(number,digit) -> int:
   """
   特定の桁の数を返す
   """
   fd = findDigit(number)
   return (number // (10**(fd-digit))) % 10

def incrementDigit(number,digit) -> int:
   """
   特定の桁の数を桁上りさせ、下の桁を0にした値を返す
   """
   fd = findDigit(number)
   return (number + 10**(fd - digit)) - (number % 10**(fd - digit))

def checkUnder(number, digit) -> bool:
   """
   指定した桁より下がすべて0か確認する関数
   """
   fd = findDigit(number)
   reminder = number - ((number//10**(fd-digit))*10**(fd-digit))
   if reminder == 0:
      ans = True
   else:
      ans = False
   return ans

def warp(number,digit) -> int:
   """
   指定した桁がインクリメントするときに、その間にヘビ数が何個あるかを返す関数
   注:必ずcheckUnderがTrueのときのみ実行
   """
   return findTopNumber(number)**(findDigit(number)-digit)

if __name__ == '__main__':

  inputNumbers = input().split()
    
  l = int(inputNumbers[0])
  r = int(inputNumbers[1]) + 1

  num = l
  count = 0

  while num < r:
    digit = findDigit(num)
    top = findTopNumber(num)
    for i in range(1,digit+1):
        if top <= findCertainNumber(num,i) and i !=1:
          # ヘビ数ではない状態
          num = incrementDigit(num,i)
          break
        elif checkUnder(num,i) and i != digit and incrementDigit(num,i) < r:
          count += warp(num,i)
          num = incrementDigit(num,i)
          break
    else:
        num = incrementDigit(num,i)
        count += 1
  print(count)
