N, K = map(int, input().split())
num = N
seen = {}
history = []
for i in range(100001):
  if num in seen:
    loopStart = seen[num]
    loopLen = i - loopStart
    break
  seen[num] = i
  history.append(num)
  
  while N > 0:
    num += N % 10
    N //= 10
  num %= 100000
  N = num

if K >= loopStart:
  index = (K - loopStart) % loopLen + loopStart
  print(history[index])
else:
  print(history[K])