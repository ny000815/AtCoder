N, M = map(int, input().split())
dist =[]
for i in range(N-1):
  dist.append(int(input()))
move = []
for i in range(M):
  move.append(int(input()))

lrCumSum, rlCumSum = [0], [0]
for i in range(N-1):
  lrCumSum.append(lrCumSum[i]+dist[i])
  rlCumSum.append(rlCumSum[i]+dist[N-2-i])
rlCumSum = rlCumSum[::-1]

pos = 1
total = 0
for i in range(M):
  nextpos = pos + move[i]
  if move[i] >= 0:
    total += lrCumSum[nextpos-1] - lrCumSum[pos-1]
  elif move[i] < 0:
    total += abs(rlCumSum[pos-1] - rlCumSum[nextpos-1])
  pos = nextpos
print(total % 100000)