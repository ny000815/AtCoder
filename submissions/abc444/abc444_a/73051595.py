N = int(input())
A = N % 10
N //= 10
B = N % 10
N //= 10
C = N 
print("Yes" if A == B == C else "No")
