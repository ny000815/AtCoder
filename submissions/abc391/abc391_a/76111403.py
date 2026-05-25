d = input()
ans = ""
for l in d:
    if l == 'N':
        ans += 'S'
    if l == 'S':
        ans += 'N'
    if l == 'W':
        ans += 'E'
    if l == 'E':
        ans += 'W'
print(ans)