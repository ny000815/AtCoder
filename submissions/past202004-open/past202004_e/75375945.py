N = int(input())
A = [0] + list(map(int, input().split()))
for i in range(1, N+1):
  cnt = 1
  j = i
  while A[i] != j:
    i = A[i]
    cnt += 1
  print(cnt)