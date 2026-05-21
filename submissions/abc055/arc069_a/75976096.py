N, M = map(int, input().split())
if M < 2:
    print(0)
    exit(0)
print(min((N + (M // 2)) // 2,M//2))