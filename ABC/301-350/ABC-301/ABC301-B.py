N = int(input())
A = list(map(int,input().split()))
ans = []

for i in range(N-1):
    ans.append(A[i])
    
    if abs(A[i]-A[i+1])!=1:
        if A[i]<A[i+1]:
            for j in range(A[i]+1,A[i+1]):
                ans.append(j)
        else:
            for j in range(A[i]-1,A[i+1],-1):
                ans.append(j)
# 最後の数字を追加
ans.append(A[N-1])
print(*ans)
