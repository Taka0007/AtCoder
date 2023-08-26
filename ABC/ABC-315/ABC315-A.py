S = input()
NG_list = ['a','e','i','o','u']
ans = ''

for i in range(len(S)):
    if S[i] not in NG_list:
        ans += S[i]
print(ans)