A, B, K = map(int, input().split())
if A < K:
    print(0, max(B - K + A, 0))
else:
    print(A-K, B)