N, D = map(int, input().split())
S = input()
cnt = 0
for l in S:
    if l == '.':
        cnt += 1
print(cnt + D)
