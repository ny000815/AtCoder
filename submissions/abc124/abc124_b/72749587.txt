N = int(input())
H = map(int, input().split())

max = 0
cnt = 0
for n in H:
  if n >= max:
    cnt += 1
    max = n
print(cnt)