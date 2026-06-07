from traceback import print_tb

N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
for i in range(1,N+1):
    if B[A[i]] != i:
        print("No")
        exit()
print("Yes")
