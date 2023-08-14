H = int(input())
W = int(input())
N = int(input())

ans = ( N//max(H,W) ) +  min(1,(N%(max(H,W))))
print(ans)