T, X = map(int, input().split())
A = list(map(int, input().split()))
currentV = A[0]
print(0, A[0])
for i in range(1,T+1):
    if abs(currentV - A[i]) >= X:
        print(i, A[i])
        currentV = A[i]