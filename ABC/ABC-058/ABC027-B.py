O = input()
E = input()
ans = ''

if len(O)==len(E):
    for i in range(len(O)):
        ans += O[i]+E[i]
        
else:
    for i in range(len(O)-1):
        ans += O[i]+E[i]
    ans += O[-1]
    
print(ans)
