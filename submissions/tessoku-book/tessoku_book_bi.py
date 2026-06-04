N, M = map(int, input().split())
ver = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    ver[A-1].append(B)
    ver[B-1].append(A)

for i in range(N):
    print(i+1, ": {", sep="", end = "")
    for j in range(len(ver[i])):
        if j == 0:
            print(ver[i][j], end = "")
        else:
            print(", ", ver[i][j], sep = "", end = "")
    print("}")