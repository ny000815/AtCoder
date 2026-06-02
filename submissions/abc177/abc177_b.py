S = input()
T = input()

result = len(T)
for i in range(len(S) - len(T) + 1):
  diff = 0
  for j in range(len(T)):
    if S[j + i] != T[j]:
      diff += 1
  result = min(diff, result)
print(result)