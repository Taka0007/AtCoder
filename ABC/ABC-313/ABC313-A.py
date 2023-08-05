N = int(input())
P = list(map(int,input().split()))

if N==1:
    ans = 0
elif max(P[1:])<P[0]:
    ans = 0
else:
    ans = max(P[1:])-P[0]+1
print(ans)