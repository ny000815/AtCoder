N = int(input())
D = list(map(int, input().split()))
for i in range(N-1):
    dist = 0
    ans = []
    for j in range(i, N-1):
        dist += D[j]
        ans.append(dist)
    print(*ans)