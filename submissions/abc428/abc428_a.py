S, A, B, X = map(int, input().split())
q = X//(A + B)
mod = X%(A + B)
print(S * (A * q + A) if mod >= A else S * (A * q + mod))