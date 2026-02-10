import math
N = int(input())

row = math.ceil(N / 9)
col = N % 9
if col == 0:
  col = 9

ans = ""
for _ in range(row):
  ans += str(col)
print(ans)