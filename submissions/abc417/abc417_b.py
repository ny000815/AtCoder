N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
skipping = [0] * len(A)
B.sort()

i = 0
j = 0
while i < N and j < M:
    if A[i] == B[j]:
        skipping[i] = 1
        i += 1
        j += 1
    elif A[i] > B[j]:
        j += 1
    else:
        i += 1
res = []
for i in range(N):
    if skipping[i]:
        continue
    res.append(A[i])
print(*res)