a,b,c = map(int,input().split())

if c == a+b and c==a-b:
    ans = '?'
    
elif c==a+b:
    ans ='+'
    
elif c==a-b:
    ans = '-'

else:
    ans = '!'
    
print(ans)
