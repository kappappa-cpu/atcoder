#https://atcoder.jp/contests/abc425/tasks/abc425_c
# ABC425 C - Rotate and Sum Query
import sys

it = iter(map(int, sys.stdin.buffer.read().split()))
N = next(it)
Q = next(it)

A = [next(it) for _ in range(N)]

# 2倍配列と累積和
B = A + A
P = [0] * (2 * N + 1)
for i, v in enumerate(B):
    P[i + 1] = P[i] + v

shift = 0
out = []

for _ in range(Q):
    t = next(it)
    if t == 1:
        c = next(it)
        shift = (shift + c) % N
    else:  # t == 2
        l = next(it)
        r = next(it)
        start = shift + (l - 1)
        end   = shift + (r - 1)
        out.append(str(P[end + 1] - P[start]))

print("\n".join(out))
  