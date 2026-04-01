digits = [-1]*3
N, M = map(int, input().split())
s, c = [],[]
for _ in range(M):
  a, b = map(int, input().split())
  s.append(a-1)
  c.append(b)

def ok(num):
  for i in range(M):
    if num[s[i]] != str(c[i]):
      return False
  return True

ans = -1
st, en = 0, 10
if N == 2:
  st, en = 10, 100
if N == 3:
  st, en = 100, 1000
for i in range(st,en):
  if ok(str(i)):
    ans = i
    break
print(ans)