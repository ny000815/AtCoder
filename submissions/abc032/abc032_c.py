N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]
for i in range(N):
    if s[i] == 0:
        print(N)
        exit()
if K == 0:
    print(0)
    exit()
left = 0
ans = 0
prod = 1
for right in range(N):
    prod *= s[right]
    while prod > K:
        prod //= s[left]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)

