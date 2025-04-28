N     = int(input())
A     = list(map(int,input().split()))
A.sort()
ans   = A[-1]
limit = 10**18

for i in range(N-1):
    ans *= A[i]
    
    if ans>limit:
        ans = -1
        break
    elif ans==0:
        ans = 0
        break
    
print(ans)