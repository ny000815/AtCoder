s = input()
isPalindrome = True
for i in range(len(s)//2):
  if s[i] == '*' or s[len(s) - i - 1] == '*':
    continue
  if s[i] != s[len(s) - i - 1]:
    isPalindrome = False
print("YES" if isPalindrome else "NO")