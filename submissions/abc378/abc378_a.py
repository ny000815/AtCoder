A = list(map(int, input().split()))
lst = [0] * 4
for a in A:
    lst[a-1] += 1
ans = 0
for n in lst:
    if n == 4:
        ans += 2
    if 2 <= n <= 3:
        ans += 1
print(ans)