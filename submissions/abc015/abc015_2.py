N = int(input())
A = list(map(int, input().split()))
cnt = 0
bugCnt = 0
for i in range(N):
  if A[i] != 0:
    cnt += 1
    bugCnt += A[i]
if bugCnt % cnt != 0:
  bugCnt += cnt
print(bugCnt//cnt)