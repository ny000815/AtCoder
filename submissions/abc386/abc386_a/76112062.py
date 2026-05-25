c = list(map(int, input().split()))
cnt = set()
for n in c:
    cnt.add(n)
print("Yes" if len(cnt) == 2 else "No")