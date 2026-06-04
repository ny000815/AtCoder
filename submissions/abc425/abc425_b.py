N = int(input())
A = list(map(int, input().split()))
lst = [0] * (N + 1)
for i in range(N):
    if A[i] == -1:
        continue
    lst[A[i]] += 1
    if lst[A[i]] == 2:
        print("No")
        exit()
print("Yes")
for i in range(N):
    if A[i] != -1:
        print(A[i], end=" ")
    else:
        for j in range(1, N + 1):
            if lst[j] == 0:
                print(j, end=" ")
                lst[j] += 100
                break