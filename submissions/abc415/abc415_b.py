S = input()
cnt = []
for i in range(len(S)):
    if S[i] == '#':
        cnt.append(i+1)
    if len(cnt) == 2:
        print(cnt[0], cnt[1], sep = ",")
        cnt = []

