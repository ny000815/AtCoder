a, b = map(int, input().split())
if a <= b:
  for _ in range(b):
    print(a, end = "")
else:
  for _ in range(a):
    print(b, end = "")