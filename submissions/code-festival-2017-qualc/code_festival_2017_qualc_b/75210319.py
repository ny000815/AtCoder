N = int(input())
A = list(map(int, input().split()))
oddnumP = 1
for i in range(N):
  if A[i] % 2 == 0:
    oddnumP *= 2
ALL = 1
for i in range(N):
  ALL *= 3
print(ALL - oddnumP)