A, B = map(int, input().split())

def solve (num):
  if num % 2 != 0:
    if (num + 1) % 4 == 0:
      b = 0
    else:
      b = 1
  else:
    if num % 4 == 0:
      b = 1 ^ (num + 1)
    else:
      b = 0 ^ (num + 1)
  return b
print(solve(B) ^ solve(A-1))