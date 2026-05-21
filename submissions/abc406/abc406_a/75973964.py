A, B, C, D = map(int, input().split())
print("No" if A < C or (A == C and D > B) else "Yes")