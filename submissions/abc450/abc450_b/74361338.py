N = int(input())
cnt = [[0] * (i + 1) + list(map(int, input().split())) for i in range(N - 1)]
#for i in range(N - 1):
  #print(cnt[i])
ans = "No"
for x in range(N):
  for y in range(x + 1, N):
    for z in range(y + 1, N):
      #print(x, y, z, cnt[x][y], cnt[y][z], cnt[x][y] + cnt[y][z], "", cnt[x][z])
      if cnt[x][y] + cnt[y][z] < cnt[x][z]:
        ans = "Yes"
print(ans)