N = int(input())

max = 0
maxnum = 1
for n in range(1, N+1):
  cnt = 0
  number = n
  while number % 2 == 0:
    cnt += 1
    number /= 2
  if cnt > max:
    max = cnt
    maxnum = n
print(maxnum)