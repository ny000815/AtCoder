N = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if a[i]%2 == 0:
        cnt += (format(a[i], 'b')[::-1].find("1"))
print(cnt)