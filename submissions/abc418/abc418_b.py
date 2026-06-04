S = input()

ans = 0
for i in range(len(S)-2):
    for j in range(i+2, len(S)):
        if S[i] != 't' or S[j] != 't':
            continue
        cnt = 0
        for k in range(i, j+1):
            if S[k] == 't':
                cnt += 1
        density = (cnt - 2)/(j-i+1-2)
        ans = max(ans, density)
print(ans)
