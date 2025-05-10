# input
N = int(input())
A = list(map(int,input().split()))
# calculation
ALL_sum = sum(A)
ans     = 0
for i in range(N):
    ans += A[i] * (ALL_sum - A[i])
# output
print(ans//2)