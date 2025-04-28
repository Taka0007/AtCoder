N,D = map(int,input().split())
num = list(map(int,input().split()))
now = -1

for i in range(1,N):
    
    if num[i] - num[i-1] <= D:
        now = num[i]
        break

print(now)
