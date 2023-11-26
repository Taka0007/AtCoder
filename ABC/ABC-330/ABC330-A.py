N,L = map(int,input().split())
A   = list(map(int,input().split()))
ans = 0

for point in A:
    if point >= L:
        ans += 1
print(ans)