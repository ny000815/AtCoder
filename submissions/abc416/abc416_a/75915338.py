N, L, R = map(int, input().split())
S = input()
isValid = True
for i in range(L - 1, R):
    if S[i] == 'o':
        continue
    isValid = False
print("Yes" if isValid else "No")