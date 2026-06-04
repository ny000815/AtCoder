S = input()
ans = ""
isReady = True
for i in range(len(S)):
    if S[i] == '#':
        ans += '#'
        isReady = True
    elif S[i] == "." and isReady:
        ans += 'o'
        isReady = False
    else:
        ans += '.'
print(ans)