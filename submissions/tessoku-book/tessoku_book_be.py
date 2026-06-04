N, Q = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(30)]
dp[0] = [0] + A

for d in range(1,30):
    for i in range(1,N+1):
        dp[d][i] = dp[d-1][dp[d-1][i]]

for _ in range(Q):
    X, Y = map(int, input().split())
    i = 0
    locations = []
    while Y > 0:
        if Y & 1:
            locations.append(i)
        Y >>= 1
        i += 1
    locations = locations[::-1]
    current = dp[locations[0]][X]
    for c in locations[1:]:
        current = dp[c][current]
    print(current)
