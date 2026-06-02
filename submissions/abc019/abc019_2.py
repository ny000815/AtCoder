S = input()
N = len(S)
i = 1
cnt = 1
curr = S[0]
res = ""
while i < N:
  if S[i] == S[i -1]:
    i += 1
    cnt += 1
  else:
    res += curr + str(cnt)
    curr = S[i]
    cnt = 1
    i += 1
res += curr + str(cnt)
print(res)