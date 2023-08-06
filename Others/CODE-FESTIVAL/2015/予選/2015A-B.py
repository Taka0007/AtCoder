N = int(input())
A = list(map(int,input().split()))
ans = 0

for i in range(N):
    ans = ans*2 + A[i]
    
print(ans)