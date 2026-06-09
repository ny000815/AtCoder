N = int(input())
P = list(map(int, input().split()))
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and P[j] > P[i]:
            rank += 1
    print(rank)