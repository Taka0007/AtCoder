N,X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    if A[i]==X:
        ans = 'Yes'
        break    
else:
    ans = 'No'
    
print(ans)


# 愚直に線形探索を実装
