N, X = map(int, input().split())
L = list(map(int, input().split()))
csum = []
csum.append(0)
for i in range (len(L)): # len(csum) == N this time
  csum.append(csum[i] + L[i])
cnt = 0
for n in csum:
  if n <= X:
    cnt += 1
print(cnt)
