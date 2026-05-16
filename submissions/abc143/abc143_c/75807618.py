N = int(input())
S = input()
curr = S[0]
res = S[0]
i = 1
while i < N:
  if S[i] == curr:
    i += 1
  else:
    res += S[i]
    curr = S[i]
print(len(res))