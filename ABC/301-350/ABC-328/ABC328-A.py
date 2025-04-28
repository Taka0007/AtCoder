N,X = map(int,input().split())
S = list(map(int,input().split()))
ans = 0

for num in S:
    if num <= X:
        ans += num

print(ans)