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

def find_nearest_character_position(char, current_i, current_j, A, N):
    min_distance = float('inf')
    target_i, target_j = -1, -1
    for i in range(N):
        for j in range(len(A[i])):
            if A[i][j] == char:
                distance = abs(i - current_i) + abs(j - current_j)
                if distance < min_distance:
                    min_distance = distance
                    target_i, target_j = i, j
    return target_i, target_j

# 操作列を生成
current_i, current_j = s_i, s_j
operations = 0

for g_str in good_str:
    for char in g_str:
        target_i, target_j = find_nearest_character_position(char, current_i, current_j, A, N)
        print(target_i, target_j)
        current_i, current_j = target_i, target_j
        operations += 1
        if operations >= 5000:
            break
    if operations >= 5000:
        break