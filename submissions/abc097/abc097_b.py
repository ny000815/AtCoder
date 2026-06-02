X = int(input())
maxnum = 1
for i in range(1, X + 1):
  for j in range(2, 100):
    if i ** j <= X:
      if i ** j >= maxnum:
        maxnum = i ** j
print(maxnum)
