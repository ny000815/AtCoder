N = int(input())
S = []
for _ in range(N):
  S.append(input())
pairs = set()
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    pairs.add(S[i]+S[j])
print(len(pairs))