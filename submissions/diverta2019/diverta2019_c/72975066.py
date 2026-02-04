N = int(input())
cnt = 0
s1, s2, s3 = 0, 0, 0
for i in range(N):
  S = input()
  cnt += S.count("AB")

  if S[0] == 'B' and S[-1] == 'A':
    s1 += 1
  elif S[0] == 'B':
    s2 += 1
  elif S[-1] == 'A':
    s3 += 1

if s2 == 0 and s3 == 0:
  print(cnt + max(s1 - 1, 0))
else:
  print(cnt + s1 + min(s2, s3))
  