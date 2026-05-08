N = int(input())
S = input()
isFirstBlock = True
for i in range(N):
  if S[i] == 'o' and isFirstBlock:
    pass
  else:
    isFirstBlock = False
    print(S[i], end = "")