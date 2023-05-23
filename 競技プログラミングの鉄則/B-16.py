N = int(input())
high = list(map(int,input().split()))
inf = 2**100
ans = [inf]*(N+1)
ans[0] = 0
ans[1] = abs(high[0]-high[1])

for i in range(1,N):
    ans[i] = min( ans[i-1]+abs(high[i]-high[i-1]) ,ans[i-2]+abs(high[i]-high[i-2]))
print(ans[N-1])
