N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
tempList = []
for n in H:
  tempList.append(T - n * 0.006)
for i in range(N):
  temp = tempList[i] - A 
  if temp < 0:
    temp *= -1
  tempList[i] = temp

print(tempList.index(min(tempList))+1)