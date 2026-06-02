N = int(input())
sq = [[0] * N for _ in range(N)]
r = 0
c = (N-1)//2
sq[r][c] = 1
for i in range(2, N**2+1):
   if sq[(r-1)%N][(c+1)%N] == 0:
       r = (r-1)%N
       c = (c+1)%N
       sq[r][c] = i
   else:
       r = (r+1)%N
       sq[r][c] = i

for row in sq:
    print(*row)