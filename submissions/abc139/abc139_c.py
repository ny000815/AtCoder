N = int(input())
S = list(map(int, input().split()))
i = 0
res = 0
while i < N:
  j = i
  while j + 1< N and S[j] >= S[j+1]:
    j += 1
  res = max(res, j - i)
  i = j + 1
print(res)