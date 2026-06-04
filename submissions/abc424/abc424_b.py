N, M, K = map(int, input().split())
players = [0]*(N+1)
ans = []
for i in range(K):
    A, B = map(int, input().split())
    players[A]+=1
    if players[A] == M:
        ans.append(A)
print(*ans)