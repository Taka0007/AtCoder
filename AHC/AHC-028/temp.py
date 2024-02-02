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


char_positions = {}
for i in range(N):
    for j in range(N):
        char = A[i][j]
        if char in char_positions:
            char_positions[char].append((i, j))
        else:
            char_positions[char] = [(i, j)]

current_i, current_j = s_i, s_j
for char in good_str:
    min_distance = float('inf')
    target_i, target_j = -1, -1

    for i, j in char_positions.get(char, []):
        distance = abs(i - current_i) + abs(j - current_j)
        if distance < min_distance:
            min_distance = distance
            target_i, target_j = i, j

    print(target_i, target_j)
    current_i, current_j = target_i, target_j