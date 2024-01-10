# input
A,B,C,D = map(int,input().split())

if A > C:
    ans = "Aoki"
elif A < C:
    ans = "Takahashi"
elif B > D:
    ans = "Aoki"
elif B < D:
    ans = "Takahashi"
else:
    ans = "Takahashi"

# output
print(ans)