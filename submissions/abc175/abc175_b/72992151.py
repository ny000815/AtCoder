N = int(input())
cnt = 0
L = list(map(int, input().split()))
L.sort()
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if L[k] < L[i] + L[j] and L[i] != L[j] and L[j] != L[k]:
        cnt += 1
print(cnt)