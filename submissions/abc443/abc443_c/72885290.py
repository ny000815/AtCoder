N, T = map(int, input().split())
A = list(map(int, input().split()))

res = 0
time = 0
A.append(T)
for i in range(N+1):
  if time < A[i]:
    res += A[i] - time
    time = A[i] + 100
  else:
    continue
print(res)