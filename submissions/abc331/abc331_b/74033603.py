N, S, M, L = map(int, input().split())
ans = 100**100
for i in range(101):
  for j in range(101):
    for k in range(101):
      if i*6 + j*8 + k*12 >= N:
        ans = min(ans, i*S + j*M + k*L)
print(ans)