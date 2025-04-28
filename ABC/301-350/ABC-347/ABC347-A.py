# input
N,K = map(int,input().split())
A   = list(map(int,input().split()))
ans = []
# output
for num in A:
    if num % K == 0:
        num //= K
        ans.append(num)
print(*ans,sep=" ")