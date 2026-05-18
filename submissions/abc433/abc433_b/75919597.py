N = int(input())
A = list(map(int, input().split()))
maxHeight = A[0]
ans = [0] * N
for i in range(0, N):
    if A[i] >= maxHeight:
        ans[i] = -1
        maxHeight = A[i]
    else:
        ans[i] = A[i]
for i in range(N-1, -1, -1):
    if ans[i] != -1:
        for j in range(i, -1, -1):
            if A[j] > A[i]:
                ans[i] = j + 1
                break
for i in range(N):
    print(ans[i])