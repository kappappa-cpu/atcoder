A=input().split()
B=A[0]
b=int(A[0])
Amax=A[1]
a=int(A[1])
startHead=int(B[0])
startLen=len(B)
maxHead=int(Amax[0])
maxLen=len(Amax)
now=[]
hozon=0
hata=False
Flag=False
kekka=0
irann=0
nowPos=0
modosi=0
zero=0

def warp(x):
  global kekka, now
  return kekka+now[0]**x

  
def makimodosi():
  '''
  数字を増やす動作を一回分キャンセルし、対象とする桁を下げる
  '''
  global nowPos, kekka, modosi
  kaunto(-1)
  nowPos=nowPos+1
  kekka=kekka-modosi
  
def ketaage():
  '''
  繰り上がり、一桁増える
  '''
  global now, nowLen
  now[0]=0
  now.insert(0,1)
  nowLen=len(now)

def kaunto(a):
  '''
  対象桁を＋aする
  '''
  global now, nowPos
  now[nowPos]=now[nowPos]+a

#初期の数字をnowに代入する
for i in range(startLen):
  now.append(int(B[i]))
nowLen=len(now)
keta=1

if startHead==maxHead and startLen==maxLen:
  giwaku=0
  koko=1
  
  while koko!=nowLen:
    if now[1]>=startHead:
      giwaku=1
      break
    if now[koko]>=startHead:
      now[koko]=0
      koko=koko-1
      now[koko]=now[koko]+1
      continue
    if now[koko]==startHead-1:
      koko=koko+1
      continue
    break
  if giwaku==1:
    print(0)
    exit()
'''
初期の数字が１００などの上一桁以外０の場合

下のwhile文２つを無視する
'''
if b%(10**(nowLen-1))==0:
  kekka=warp(nowLen-1)
  modosi=now[0]**(nowLen-1)
  irann=1
  
'''
上一桁と桁が同じの場合の問題を解決するための機構
'''
if startHead==maxHead and startLen==maxLen and irann==0:

  koko=nowLen
  hataouji=False
  #ワープはその桁のその数を次の数にするまでをカウントしたもの
  while koko>1:
    if hataouji==False:
      #ここは最初の数を整える場所、一度しか作動しないようになっている
      #あとは天井をつけることに気をつけておけば通常のワープ計算と変わらないはず
      hataouji=True
      while now[koko-1]<startHead:
        now[koko-1]=now[koko-1]+1
        kekka=kekka+1
      now[koko-1]=0
      koko=koko-1
      now[koko-1]=now[koko-1]+1
    if koko<=2 and now[koko-1]>=startHead-1:

      print(kekka)
      exit()
      #ここが天井部分、二桁目に到達したら入るようになってる
    #この下が主な計算の部分
    if koko!=2 and now[koko-1]>=startHead:
      while koko!=2 and now[koko-1]>=startHead-1:
        now[koko-1]=0
        koko=koko-1
      continue
    kekka=warp(nowLen-koko)
    now[koko-1]=now[koko-1]+1
    if koko!=2 and now[koko-1]>=startHead-1:
      now[koko-1]=0
      koko=koko-1

while keta < nowLen and startHead==now[0] and irann==0:
  #ワープの下準備場
  if now[0]<=now[keta]:
    now=now[0:keta]
    for j in range(nowLen-keta):
      now.append(0)
      zero=zero+1
    now[keta-1]+=1
    hozon=keta-1
    keta=keta-2
    
  if nowLen-1==keta and hozon==0:
    hozon=keta
    zero=0
    
  keta=keta+1
  
'''
上のは下準備、蛇数じゃない数字がある場合そこ以下を０にするはず、よく覚えていない
'''
'''
上のwhile文で０にならなかった部分を桁を上げるまで計算して強引に１０のn乗にするwhile文
'''
#ここ一旦消しているものの他の例では必と思われるためif条件を練り直すこと
#if startHead==now[0] and hozon!=0 and irann==0:
  #kekka=kekka+1

while startHead==now[0] and hozon!=0 and irann==0 :
  if now[hozon]>=startHead:
    now[hozon]=0
    hozon=hozon-1
    #この下2行は急遽追加したもののため問題起きそうで怖い、ところ問題は起きていない
    now[hozon]=now[hozon]+1
    zero=zero+1
    continue
  kekka=warp(zero)
  now[hozon]=now[hozon]+1

 
#ここで最初の数字を上一桁が変わるまで計算していく

'''
桁上がりや繰り上がりの処理が不要な場合の終了措置
'''
if startHead==maxHead or startLen==maxLen:
  kekka=kekka-modosi
#この下のifなんか雑で怖いから後で直しておこう
if startHead!=maxHead and startLen!=maxLen:
  now[0]=startHead+1
  
 
if now[0]==10:
  for i in range(nowLen):
    now[i]=0
  now.insert(0,1)
  nowLen=len(now)
#ここは１０超えてたら繰り上げて下全部０にするところ
    
if int(Amax[0]) <= int(Amax[1]):
  Flag=True

while nowPos!=maxLen or now[nowLen-1]!=int(Amax[maxLen-1]):
  
  kekka=warp(nowLen-(nowPos+1))
  modosi=now[0]**(nowLen-(nowPos+1))
  kaunto(1)
  
  if nowLen==maxLen and (now[nowPos]>int(Amax[nowPos]) or now[nowPos]>int(Amax[0])):
    if Flag==True:
      print(kekka)
      exit()
    makimodosi()
    continue
  
  if now[0]==10:
    ketaage()
    
  if now[0] <= now[nowPos] and nowPos >= 1:
    print(kekka)
    exit()

kekka=kekka+1
for i in range(1,nowLen-1):
  if now[0]<=now[i]:
    kekka=kekka-1
    break
print(kekka)