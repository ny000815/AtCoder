N, M = map(int, input().split())
C = list(map(int, input().split()))
A, B = [], []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

ans = 0
for i in range(N):
  qty = min(C[A[i]-1],B[i])
  if qty > 0:
    C[A[i]-1] -= qty
    ans += qty
print(ans)
