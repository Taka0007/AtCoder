S = input()
N = len(S)
ans = ''
for i in range(N):
    if S[i]=='0':
        ans += '0'
    elif S[i]=='1':
        ans += '1'
    else:
        if len(ans)!=0:
            ans = ans[:-1]
print(ans)