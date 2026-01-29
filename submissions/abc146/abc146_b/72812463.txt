N = int(input())
S = input()
res = ""
for n in S:
  letter = ord(n) - ord("A")
  letter = (letter + N) % 26
  res += chr(letter + ord("A"))
print(res)