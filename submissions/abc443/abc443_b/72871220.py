N, K = map(int, input().split())
i = N + 1
cnt = 0
while N < K:
  N += i
  i += 1
  cnt += 1
print(cnt)