# Problem link    : https://atcoder.jp/contests/abc041/tasks/abc041_b
# Submission link : https://atcoder.jp/contests/abc041/submissions/51539785

# input
A,B,C = map(int,input().split())
# output
mod = 10**9 + 7
ans = ((A%mod) * (B%mod) * (C%mod)) % mod
print(ans)