N = int(input())
A = list(map(int, input().split()))

s = sum(A)
sq = sum(n * n for n in A)
ans = N * sq - s * s
print(ans)