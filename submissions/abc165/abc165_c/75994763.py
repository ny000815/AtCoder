from itertools import combinations_with_replacement
N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    A, B, C, D = map(int, input().split())
    a.append(A-1)
    b.append(B-1)
    c.append(C)
    d.append(D)
def calc(arr):
    score = 0
    for ai, bi, ci, di, in zip(a, b, c, d):
        if arr[bi] - arr[ai] == ci:
            score += di
    return score

maxScore = 0
for A in combinations_with_replacement(range(1, M + 1), N):
    maxScore = max(calc(A), maxScore)
print(maxScore)


