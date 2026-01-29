S = input()
slen = len(S)
cnt = 0
for i in range(len(S)//2):
  if S[i] != S[slen -1 - i]:
    cnt += 1
print(cnt)