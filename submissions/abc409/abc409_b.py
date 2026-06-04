N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
for i in range(N, -1, -1):
    if A[i-1]>=i:
        print(i)
        exit()
