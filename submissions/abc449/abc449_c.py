N, L, R = map(int, input().split())
S = input()
ans = 0
cnt = [0]*26
for i in range(N):
  if i >= L:
    cnt[ord(S[i - L]) - ord('a')] += 1
  if i > R:
    cnt[ord(S[i - R - 1]) - ord('a')] -= 1
  ans += cnt[ord(S[i]) - ord('a')]
print(ans)