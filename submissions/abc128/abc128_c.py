N, M = map(int, (input().split()))
k, s = [], []
for i in range(M):
    tmp = list(map(int, input().split()))
    k.append(tmp[0])
    s.append([a - 1 for a in tmp[1:]])
p = list(map(int, input().split()))

ans = 0
for bit in range(1 << N):
    ok = True
    for i in range(M):
        num = 0
        for bulb in s[i]:
            if bit&(1<<bulb):
                num += 1
        if num % 2 != p[i]:
            ok = False
    if ok:
        ans += 1
print(ans)
