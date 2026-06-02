N = int(input())
ans = set()
for i in range(N):
  a = list(map(int, input().split()))
  ans.add("".join(str(a[1:])))
print(len(ans))