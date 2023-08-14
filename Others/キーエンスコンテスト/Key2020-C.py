N,K,S = map(int,input().split())

if S==10**9:
    pre1 = [S]*K
    pre2 = [1]*(N-K)
    ans = pre1 + pre2
else:
    pre1 = [S]*K
    pre2 = [S+1]*(N-K)
    ans = pre1 + pre2
print(*ans)