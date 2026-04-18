N, M = map(int, input().split())
F = list(map(int, input().split()))
ansA = True
ansB = True

kinds = set()
for i in range(N):
  if F[i] in kinds:
    ansA = False
  kinds.add(F[i])
if len(kinds) < M:
  ansB = False
print("Yes"if ansA else "No")
print("Yes"if ansB else "No")