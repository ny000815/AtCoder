N, X = input().split()
N = int(N)
num = ord(X) - ord('A')
for i in range(N):
    s = input()
    if s[num] == 'o':
        print("Yes")
        exit(0)
print("No")