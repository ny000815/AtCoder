N = int(input())
L = list(map(int, input().split()))
ans = N-1
for i in range(N):
    if L[i] == 0:
        ans -= 1
    else:
        break
for j in range(N-1, -1, -1):
    if L[j] == 0:
        ans = max(0, ans-1)
    else:
        break
print(ans)