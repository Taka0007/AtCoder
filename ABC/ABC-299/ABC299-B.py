N,T = map(int,input().split())
col = list(map(int,input().split()))
num = list(map(int,input().split()))

if T in set(col):
    
    for i in range(N):
        if col[i]!=T:
            num[i]=-1
else:
    for i in range(1,N):
        if col[i]!=col[0]:
            num[i]=-1
            
ans = num.index(max(num))+1
print(ans)
        
