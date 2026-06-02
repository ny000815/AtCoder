import sys
sys.setrecursionlimit(1000000) 
N = int(input())
ans = 0

def findNum(num, has3, has5, has7):
  global ans
  if num > N:
    return
  if has3 and has5 and has7:
    ans += 1
  findNum(num*10 + 3, True, has5, has7)
  findNum(num*10 + 5, has3, True, has7)
  findNum(num*10 + 7, has3, has5, True)

findNum(0, False, False, False)
print(ans)