N = int(input())
A = list(map(int, input().split()))
for i in range(2, N):
    if A[i - 2] == A[i - 1] and A[i - 1] == A[i]:
        print("Yes")
        exit()
print("No")