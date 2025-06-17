import math

def findDigit(number):
  return math.ceil(math.log10(number+0.1))

def findTopNumber(number):
  return number//10**(findDigit(number)-1)

def normalCount(num_,count_,ft_, fd_):
    under = num_ - ft_ * (10** (fd_-1))
    for i in list(str(under)):
      if ft_ <= int(i):
        break
    else:
      count_+=1
      
    num_+=1 
    return num_, count_
  

  
l = 252509054433933519
r = 760713016476190692 + 1

num = l
count = 0

while num < r:
    ft = findTopNumber(num)
    fd = findDigit(num)
    nextLarge = (ft + 1)*10**(fd-1)
    check = True if nextLarge < r else False
    print(num, count, ft, fd, nextLarge, check)
    under = num - ft * (10** (fd-1))
    # print("under:", set(list(str(under))))
    """
    2521のnextLargeが3000、2600、2530になるまでの再帰的な関数を実装する
    """
    if set(list(str(num - ft * (10** (fd-1))))) == {'0'} and check:
        print("ワープ")
        count += ft ** (fd -1)
        num = nextLarge
    else:
        num,count = normalCount(num,count,ft, fd)

print(count)
