N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
maximum = A[-1]
cumSum = [0]
for i in range(N):
    cumSum.append(A[i] + cumSum[i])

def binSearch(n, arr):
  length = len(arr)
  left = -1
  right = length
  mid = (right + left)//2
  while right - left > 1:
    if arr[mid] >= n:
      right = mid
    else:
      left = mid
    mid = (right + left)//2
  return left

for i in range(Q):
  B = int(input())
  if B > maximum:
    print(-1)
  else:
    pos = binSearch(B, A)
    #print(pos)
    ans = cumSum[pos+1] + (B - 1)*(N - pos - 1) + 1
    print(ans)