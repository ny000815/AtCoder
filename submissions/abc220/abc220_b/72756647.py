K = int(input()) 
A, B = map(int, input().split())
resA = 0
resB = 0
for i in range(len(str(A))):
  if i == 0:
    resA += A % 10
  else:
    resA += A  % 10 * K ** i
  A //= 10
for i in range(len(str(B))):
  if i == 0:
    resB += B % 10
  else:
    resB += B  % 10 * K ** i
  B //= 10
print(resA * resB)