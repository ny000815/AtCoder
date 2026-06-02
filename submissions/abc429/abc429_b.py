N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if sum(A[:i]) + sum(A[i+1:]) == M:
        print("Yes")
        exit()
print("No")