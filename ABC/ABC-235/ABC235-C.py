from collections import defaultdict

N,Q    = map(int,input().split())
A      = list(map(int,input().split()))
A_dict = defaultdict(list)

for i in range(N):
    A_dict[A[i]].append(i+1)
    
for _ in range(Q):
    query = list(map(int,input().split()))
    
    if len(A_dict[query[0]])==0 or query[1] > len(A_dict[query[0]]):
        ans = -1
    else:
        ans = A_dict[query[0]][query[1]-1]
        
    print(ans)