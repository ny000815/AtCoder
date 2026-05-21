N, S = map(int, input().split())
T = list(map(int, input().split()))

upUntil = S
for i in range(0, N):
    if T[i] > upUntil:
        print("No")
        exit()
    else:
        upUntil = T[i] + S
print("Yes")