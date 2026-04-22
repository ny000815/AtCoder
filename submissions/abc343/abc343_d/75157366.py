from collections import defaultdict
N, T = map(int, input().split())
num = [0] * N
score_count = defaultdict(int)
score_count[0] = N

for i in range(T):
  A, B = map(int, input().split())
  A -= 1
  old = num[A]
  new = num[A] + B
  score_count[old] -= 1
  if score_count[old] == 0:
    del score_count[old]
  num[A] = new
  score_count[new] += 1
  print(len(score_count))