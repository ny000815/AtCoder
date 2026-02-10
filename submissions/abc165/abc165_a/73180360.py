K = int(input())
A, B = map(int, input().split())

isValid = False

if B // K != A // K or A % K == 0 or B % K == 0:
  isValid = True

print("OK" if isValid else "NG")
