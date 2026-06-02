N = int(input())
A = list(map(int, input().split()))
cutPoint = [0]
angle = 0
for i in range(N):
  angle += A[i]
  angle %= 360
  cutPoint.append(angle)
cutPoint.sort()
angles = []
for i in range(1,N + 1):
  if i == N:
    angles.append(360 - cutPoint[i])
  angles.append(cutPoint[i] - cutPoint[i - 1])
print(max(angles))