S = input()
T = input()
S1 =[]
T1 =[]
for i in range(len(S)):
  if S[i] == 'A':
    continue
  S1.append(S[i])
for i in range(len(T)):
  if T[i] == 'A':
    continue
  T1.append(T[i])


  
if S1 != T1:
  print(-1)
else:
  S2 = []
  T2 = []
  cnt = 0
  for i in range(len(S)):
    if S[i] == 'A':
      cnt += 1
    if S[i] != 'A':
      S2.append(cnt)
      cnt = 0
    if i == len(S) -1:
      S2.append(cnt)
  cnt = 0
  for i in range(len(T)):
    if T[i] == 'A':
      cnt += 1
    if T[i] != 'A':
      T2.append(cnt)
      cnt = 0
    if i == len(T) -1:
      T2.append(cnt)
  
  ans = 0
  for i in range(len(S2)):
    ans += abs(S2[i] - T2[i])
  print(ans)