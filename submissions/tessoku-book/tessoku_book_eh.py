N, M = map(int, input().split())
friend_cnt = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    friend_cnt[A] += 1
    friend_cnt[B] += 1
print(friend_cnt.index(max((friend_cnt))))