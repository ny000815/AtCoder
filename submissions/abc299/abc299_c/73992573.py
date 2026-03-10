N = int(input())
S = input()
maxlen = 0
cnt = 0
for i in range(N):
  if S[i] == 'o':
    cnt += 1
  if S[i] == '-':
    maxlen = max(maxlen, cnt)
    cnt = 0
cnt = 0
isDango = False
for i in range(N):
  if S[i] == 'o' and isDango:
    cnt += 1
    maxlen = max(maxlen, cnt)
  if S[i] == '-':
    cnt = 0
    isDango = True
print(maxlen if maxlen != 0 else -1)