N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = [2**200]*(N+1)
ans[0] = 0
ans[1] = A[0]

for i in range(2,N):
    ans[i] = min(ans[i-1]+A[i-1], ans[i-2]+B[i-2])
    
print(ans[N-1])


# 基本的な動的計画法
