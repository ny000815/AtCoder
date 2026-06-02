lengths = {}
arrays = {}

N, K = map(int, input().split())
for i in range(N):
  row = list(map(int, input().split()))
  L = row[0]
  A = row[1:]
  lengths[i] = L
  arrays[i] = A

C = list(map(int, input().split()))


curr = 0;
for i in range(N):
  L = lengths[i]
  blockLen = L * C[i]
  if K > blockLen:
    K -= blockLen
  else:
    print(arrays[i][(K - 1) % L])
    break