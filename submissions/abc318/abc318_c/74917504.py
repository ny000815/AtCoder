N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True)
cumSum = [0]
for i in range(N):
  cumSum.append(cumSum[i] + F[i])
ans = cumSum[N]
for i in range((N + D - 1)//D + 1):
  passCost = P * i
  covered = min(D * i, N)
  normalCost = cumSum[N] - cumSum[covered]
  ans = min(ans, passCost+normalCost)
print(ans)