N = int(input())
kindsSet = set()
items = list(map(int, input().split()))
for item in items:
  kindsSet.add(item)
  
print("YES" if len(kindsSet) == N else "NO")