N = int(input())
cnt = 0
for _ in range(N):
    A, B = map(int, input().split())
    if A < B:
       cnt += 1
print(cnt)