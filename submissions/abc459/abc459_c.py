N, Q = map(int, input().split())
lst = [0] * N
baseMinus = 0
cnt = [0] * (Q + 2)
cnt[0] = N

for i in range(Q):
    qt, qn = map(int, input().split())
    if qt == 1:
        lst[qn - 1] += 1
        cnt[lst[qn - 1]] += 1
        if cnt[baseMinus+1] == N:
            baseMinus += 1
    if qt == 2:
        i = qn + baseMinus
        if i > Q:
            print("0")
        else:
          print(cnt[qn + baseMinus])
