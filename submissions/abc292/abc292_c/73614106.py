N = int(input())

def dNum(num):
    d = [0] * num
    for i in range(1, num):
        for j in range(i, num, i):
            d[j] += 1
    return d

d = dNum(N)
ans = 0
for x in range(1, N):
    y = N - x
    ans += d[x] * d[y]
print(ans)