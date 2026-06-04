N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
if N>K:
    A = A[:-(N-K)]
A = A[::-1]
total = 0
for i in range(K):
    total += A[i]
    if total >= X:
        print(i+1+(N-K))
        exit()
print(-1)