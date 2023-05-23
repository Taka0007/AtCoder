N = int(input())
ans = ''

for i in range(9,-1,-1):
    pre = (N//(2**i))%2
    ans += str(pre)
    
print(ans)
