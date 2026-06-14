N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

i , j = 0, 0
ans = 0
while i < len(A) and j < len(B):
  if A[i] >= B[j]:
    ans += A[i]
    j += 1
  i += 1
print(ans if j == len(B) else -1)