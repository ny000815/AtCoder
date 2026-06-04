N = int(input())

def rotate90(S):
    ans = []
    for s in zip(*S[::-1]):
        ans.append(s)
    return ans
def checkdiff(S, T):
    diff = 0
    for si, ti in zip(S, T):
        for sij, tij in zip(si, ti):
            if sij != tij:
                diff += 1
    return diff

S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

ans = checkdiff(S, T)
for i in range(1,4):
    S = rotate90(S)
    ans = min(ans, checkdiff(S, T)+i)

print(ans)