N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
su = sum(A[:K])
for i in range(K, N+1):
  su = su - A[i-K] + A[i]
  print(su)