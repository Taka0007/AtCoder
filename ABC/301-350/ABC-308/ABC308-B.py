N,M = map(int,input().split())
# 食べた皿の色
C = list(map(str,input().split()))
# 色の定義
D = list(map(str,input().split()))
# 色ごとの値段
P = list(map(int,input().split()))
price = 0

for i in range(N):
    try:
        price += P[D.index(C[i]) + 1]
    except ValueError:
        price += P[0]
print(price)