N = int(input())
S = input()

if S.count('A') > S.count('T'):
    ans = 'A'
elif S.count('A') < S.count('T'):
    ans = 'T'
else:
    for i in range(N):
        newS = S[:i]
        
        if newS.count('A')==N//2:
            ans = 'A'
            break
        elif newS.count('T')==N//2:
            ans = 'T'
            break
print(ans)
