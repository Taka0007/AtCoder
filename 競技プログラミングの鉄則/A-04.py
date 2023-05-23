N = int(input())
ans = ''

for i in range(9,-1,-1):
    pre = (N//(2**i))%2
    ans += str(pre)
    
print(ans)

# 10進法を2進法に変換
# rangeの範囲を変更するともっとNが大きくなっても対応できる
