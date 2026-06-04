S = input()
cnt = 0
ans = 0

for i in range(len(S)):
    if S[i] == 'B':
        cnt += 1
    if S[i] == 'W':
        ans += cnt
print(ans)
