S   = input()
c   = input()
ans = ''

for i in range(len(S)):
    if S[i]==c:
        ans += c*2
    else:
        ans += S[i]
print(ans)