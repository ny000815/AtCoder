A = list(map(int, input().split()))
cnt = [0 for _ in range(13)]
for i in range(7):
    cnt[A[i]-1] += 1
has3, has2 = False, False
for i in range(13):
    if cnt[i] >= 3 and not has3:
        has3 = True
    elif cnt[i] >= 2:
        has2 = True
print("Yes" if has3 and has2 else "No")