N, Q = map(int, input().split())
X = list(map(int, input().split()))
box = [0] * N
ans = []
for i in range(Q):
    if X[i] >= 1:
        box[X[i] - 1] += 1
        ans.append(X[i])
    else:
        ans.append(box.index(min(box))+1)
        box[box.index(min(box))] += 1
print(*ans)