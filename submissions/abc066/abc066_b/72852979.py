def eves_check(st):
  num = len(st)
  for i in range(num // 2):
    if num % 2:
      return False
    if st[i] != st[num // 2 + i]:
      return False
  return True
  
S = input()
res = 0
for i in range(len(S) - 1):
  if eves_check(S[0:i]) and i > res:
    res = i
print(res)