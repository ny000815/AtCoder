N, K = map(int, input().split())
A = list(map(int, input().split()))
current = 1
for i in range(N):
    current *= A[i]
    if len(str(current)) > K:
        current = 1
print(current)