N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        isOK = True
        s = sum(A[i:j+1])
        if all(s % A[k] != 0 for k in range(i, j+1)):
            ans += 1
print(ans)