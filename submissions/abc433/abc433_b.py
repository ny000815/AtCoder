N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    ans = -1
    for j in range(i, -1, -1):
        if A[j] > A[i]:
            ans = j + 1
            break
    print(ans)