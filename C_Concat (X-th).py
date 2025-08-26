# https://atcoder.jp/contests/abc416/tasks/abc416_c
# C - Concat (X-th)

def carryUp(idx:list) -> list:
  '''
  [0,2,2,...]という数値の組をn進数と捉えて、mod k 上で +1したリストを返す
  例えば[0,2,2]をmod3上+1すると、[1,0,0]が返る
  '''
  
  now_digit = k-1
  flag = True
  while flag:
    flag = False
    if (idx[now_digit]+1)%n == 0:
      flag = True
      idx[now_digit] = 0
      now_digit -= 1
    else:
      idx[now_digit] +=1
    if now_digit == -1:
      flag = False
  return idx

if __name__ == '__main__': 
    n, k, x = map(int,input().split())

    slist = [input().strip() for _ in range(n)]

    idx = [0]*k
    cands = []
    i = 0
    # すべての文字列の組み合わせを作ってからsortしてx番目を出力
    while i < n**k:
        cands.append(''.join(slist[j] for j in idx))
        idx = carryUp(idx)
        i += 1
    cands.sort()
    print(cands[x-1])