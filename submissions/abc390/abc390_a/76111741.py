A = list(map(int, input().split()))
sortedA = sorted(A)
diff = 0
for i in range(1, len(A)):
    tmp = A.copy()
    A[i], A[i-1] = A[i-1], A[i]
    if A == sortedA:
        print("Yes")
        exit()
    A = tmp
print("No")