# input
A,B,C,D = map(int,input().split())
MOD = 998244353
# 階乗・逆元階乗の前計算
N   = A+B+C+D
fact = [1]*(N+1)
invf = [1]*(N+1)
for i in range(1, N+1):
    fact[i] = fact[i-1]*i % MOD
invf[N] = pow(fact[N], MOD-2, MOD)
for i in range(N, 0, -1):
    invf[i-1] = invf[i]*i % MOD

def nCr(n,r):
    if r<0 or r>n: return 0
    return fact[n]*invf[r]%MOD*invf[n-r]%MOD

if D == 0:
    ans = nCr(A+B+C, A+C)
else:
    ans = 0
    for k in range(C+1):
        ans += nCr(A+B+k, A+k) * nCr(C-k+D-1, D-1)
        ans %= MOD
print(ans)