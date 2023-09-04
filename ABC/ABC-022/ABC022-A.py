N,S,T = map(int,input().split())
ans   = 0
W     = 0
def Best_Body(weight):
    if weight>=S and weight<=T:
        return True
    else:
        return False

for i in range(N):
    a = int(input())
    W += a
    if Best_Body(W):
        ans += 1
print(ans)