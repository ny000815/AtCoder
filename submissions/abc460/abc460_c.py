N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

ans = 0
i = 0
j = 0
while i < N and j < M:
    if A[i] * 2 >= B[j]:
        i += 1
        j += 1
        ans += 1
    else:
        j += 1
print(ans)