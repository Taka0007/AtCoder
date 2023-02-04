N,K = map(int,input().split())
name = []
ans = []

for i in range(N):
    S = input()
    name.append(S)
    
for i in range(K):
    ans.append(name[i])
    
ans.sort()
   
for i in ans:
    print(i)
