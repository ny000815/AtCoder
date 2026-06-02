N = int(input())
S = input()
prefix = [0]
for i in range(N):
  prefix.append(prefix[i] + 1 if S[i] == 'W' else prefix[i])
ans = 10**100
for i in range(N):
  left = prefix[i]
  right = N - i - 1 - (prefix[N] - prefix[i+1])
  ans = min(ans, left+right)
print(ans)