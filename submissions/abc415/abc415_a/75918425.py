N = int(input())
A = list(map(int, input().split()))
X = int(input())

isValid = False
for i in range(N):
    if A[i] == X:
        isValid = True
print("Yes" if isValid else "No")