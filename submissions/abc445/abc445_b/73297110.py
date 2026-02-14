N = int(input())
S = []
maxlen = -1
for i in range(N):
  S.append(input())
  maxlen = max(maxlen, len(S[i]))

for i in range(N):
  for _ in range((maxlen - len(S[i])) // 2):
    print('.', end = "")
  print(S[i], end = "")
  for _ in range((maxlen - len(S[i])) // 2):
    print('.', end = "")
  print("")