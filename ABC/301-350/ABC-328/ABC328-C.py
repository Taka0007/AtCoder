N,Q = map(int,input().split())
S = input()
ans = [0]*N
queries = []

# 累積和の計算
ans[0] = 0
for i in range(1,N):
    if S[i-1] == S[i]:
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = ans[i-1]

for i in range(Q):
    l,r   = map(int,input().split())
    ANS = ans[r-1] - ans[l-1]
    print(ANS)