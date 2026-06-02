S = input()

cnt = 0
ans = []
for i in range(1, len(S)):
  if S[i] == '-':
    cnt += 1
  elif S[i] == '|':
    ans.append(cnt)
    cnt = 0
print(*ans)