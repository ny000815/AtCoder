A, B, C, K = map(int, input().split())
if K <= A:
    print(K)
    exit(0)
if K <= A + B:
    print(A)
    exit(0)
print(A - (K - A - B))
