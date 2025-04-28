H,W = map(int,input().split())
#2次元配列の宣言
S = []
for _ in range(H):
    st = list(map(str,input().split()))
    S.append(st)

# 左上から全探索
ans = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            if (i!=0 and j!=0):
                if S[i-1][j] != '#' and S[i][j-1] != '#' and S[i-1][j-1] != '#':
                    ans += 1
print(ans)