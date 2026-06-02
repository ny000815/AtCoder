N, M = map(int, input().split())
H = list(map(int, input().split()))

pathGraph = [[]*N for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  pathGraph[A].append(B)
  pathGraph[B].append(A)
  
ans = 0
for i in range(N):
  isGood = True
  for j in pathGraph[i]:
    if H[j] >= H[i]:
      isGood = False
  if isGood:
    ans += 1

print(ans)