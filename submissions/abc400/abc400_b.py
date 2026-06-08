N, M = map(int, input().split())
ans = sum(N ** i for i in range(M+1))
print(ans if ans <= 10 ** 9 else "inf")