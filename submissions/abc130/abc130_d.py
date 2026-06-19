N, K = map(int, input().split())
a = list(map(int, input().split()))
left = 0
total = 0
ans = 0
for right in range(N):
    total += a[right]
    gap = len(a) - right
    while total >= K:
        ans += gap
        total -= a[left]
        left += 1
print(ans)