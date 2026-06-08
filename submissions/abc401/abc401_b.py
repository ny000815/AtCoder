N = int(input())
isOnline = False
cnt = 0
for _ in range(N):
    S = input()
    if not isOnline and S == "private":
        cnt += 1
    if S == "login":
        isOnline = True
    if S == "logout":
        isOnline = False
print(cnt)

