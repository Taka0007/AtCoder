# Problem link    : https://atcoder.jp/contests/abc177/tasks/abc177_c
# Submission link : https://atcoder.jp/contests/abc177/submissions/60815345

# input
N = int(input())
A = list(map(int,input().split()))
# declare variable
ans = 0
mod = 10**9 + 7
lis_sum = sum(A)
# calc ans
for i in range(N):
    lis_sum -= A[i]
    temp_sum = lis_sum % mod
    ans += A[i] * temp_sum
    ans %= mod
# output
print(ans)
