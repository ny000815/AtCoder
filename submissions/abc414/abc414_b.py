N = int(input())
ans = ""
for i in range(N):
    l, n = input().split()
    n = int(n)
    if len(ans) + n > 100:
        print("Too Long")
        exit()
    else:
        ans += l * n
print(ans)
