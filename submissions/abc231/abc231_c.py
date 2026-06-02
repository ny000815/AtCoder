from bisect import bisect_left
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
  left, right = -1, N
  x = int(input())
  while right - left > 1:
    mid = (left + right) // 2
    if x <= A[mid]:
      right = mid
    else:
      left = mid
  print(N - right)