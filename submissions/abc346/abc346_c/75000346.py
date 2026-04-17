N, K = map(int, input().split())
A = list(map(int, input().split()))
deductNum = set()
ans = K * (K + 1) // 2
for i in range(N):
  if not A[i] in deductNum and A[i] <= K:
    ans -= A[i]
    deductNum.add(A[i])
print(ans)