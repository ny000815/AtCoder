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

def rec(arr):
    if len(arr) == N:
        return calc(arr)
    max_score = 0
    prev = arr[-1] if arr else 1
    for x in range(prev, M+1):
        arr.append(x)
        max_score = max(rec(arr), max_score)
        arr.pop()
    return max_score

print(rec([]))
