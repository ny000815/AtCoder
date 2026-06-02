P, Q = map(int, input().split())
X, Y = map(int, input().split())

print("Yes" if P <= X < 100 + P and Q <= Y < 100 + Q else "No")