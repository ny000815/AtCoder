N = int(input())
subList = list(map(int, input().split()))

subNum = [0]*N 

for i in subList:
  i -= 1
  subNum[i] += 1

for n in subNum:
  print(n)