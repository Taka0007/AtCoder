# import
# ---------
import string
# ---------


# input
# ---------
N,M = map(int,input().split())

# 初期状態の指の位置
s_i, s_j = map(int,input().split())

# キーボードの座標
A = [list(input()) for _ in range(N)]

# 縁起のいい文字列一覧
good_str = [input() for _ in range(M)]
# ---------

# 頻繁に出現する文字を探す
char_count = {}
for g_str in good_str:
    for char in g_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# 最も頻繁に出現する文字を選択
most_frequent_char = max(char_count, key=char_count.get)

# 操作列を生成
current_i, current_j = s_i, s_j
for _ in range(100):
    # グリッド上で最も近い most_frequent_char を探す
    min_distance = float('inf')
    target_i, target_j = -1, -1
    for i in range(N):
        for j in range(N):
            if A[i][j] == most_frequent_char:
                distance = abs(i - current_i) + abs(j - current_j)
                if distance < min_distance:
                    min_distance = distance
                    target_i, target_j = i, j

    # 移動する
    print(target_i, target_j)
    current_i, current_j = target_i, target_j