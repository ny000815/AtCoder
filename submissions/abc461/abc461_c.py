N, K, M = map(int, input().split())
jewels = []
for i in range(N):
    c, v = map(int, input().split())
    jewels.append([v,c])
jewels.sort(reverse=True)
used = set()
cnt = 0
ans = 0
for i in range(N):
    if jewels[i][1] not in used and len(used) < M:
        used.add(jewels[i][1])
        ans += jewels[i][0]
        jewels[i][0] = 0
        cnt += 1
jewels.sort(reverse=True)

i = 0
while cnt < K:
    ans += jewels[i][0]
    i += 1
    cnt += 1
print(ans)
