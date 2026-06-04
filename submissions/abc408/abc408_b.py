N = int(input())
A = list(map(int,input().split()))
nums = set()
for a in A:
    nums.add(a)
print(len(nums))
print(*sorted(nums))