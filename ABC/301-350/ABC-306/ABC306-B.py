st = list(map(int,input().split()))
ans = 0

for i in range(len(st)):
    ans += st[i]*(2**i)

print(ans)