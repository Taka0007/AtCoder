n,a,b = map(int,input().split())

if a+b<=n:
    ans = 0
else:
    ans = (a+b)-n
print(ans)