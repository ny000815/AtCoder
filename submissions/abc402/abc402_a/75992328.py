S = input()
res = ""
for i in range(len(S)):
    if 'A' <= S[i] <= 'Z':
        res += S[i]
print(res)