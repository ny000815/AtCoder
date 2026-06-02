N = int(input())
A = list(map(int, input().split()))

pos = [-1] * N
for i in range(N):
  pos[A[i] - 1] = i

ans = []
for i in range(N):
  if A[i] == i + 1:
    continue
  temp = A[i]
  ans.append((pos[temp - 1] + 1, pos[i]+1))
  A[i] = i + 1
  A[pos[i]] = temp
  pos[i], pos[temp - 1] = i, pos[i]

print(len(ans))
for pair in ans:
  print(*pair)