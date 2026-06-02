S = input()
N = len(S)
res = 0
for i in range(N):
  if S[i] == 'C':
    res += min(N - i - 1, i) + 1
print(res)