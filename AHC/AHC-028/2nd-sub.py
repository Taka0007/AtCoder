def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def find_nearest_string(current_pos, strings, positions):
    nearest_string = None
    min_distance = float('inf')
    for s in strings:
        distance = calculate_distance(current_pos, positions[s[0]]) # 最初の文字に基づいて距離を計算
        if distance < min_distance:
            min_distance = distance
            nearest_string = s
    return nearest_string

# キーボードの座標をキャッシュする関数
def cache_keyboard_positions(A):
    positions = {}
    for i, row in enumerate(A):
        for j, char in enumerate(row):
            positions[char] = (i, j)
    return positions

# 最近接文字の位置を探す関数
def find_nearest_character_position(char, current_i, current_j, positions):
    target_i, target_j = positions[char]
    return target_i, target_j

# 入力部分
N, M = map(int, input().split())
s_i, s_j = map(int, input().split())
A = [list(input()) for _ in range(N)]
good_str = [input() for _ in range(M)]

positions = cache_keyboard_positions(A)

# ソートされた文字列のリストを初期化
sorted_strings = []

# 初期位置を設定
current_pos = (s_i, s_j)

while good_str:
    nearest_str = find_nearest_string(current_pos, good_str, positions)
    sorted_strings.append(nearest_str)
    good_str.remove(nearest_str)
    current_pos = positions[nearest_str[-1]]  # 最後の文字の位置を更新

# タイピングのシミュレーション
current_i, current_j = s_i, s_j
operations = 0

for g_str in sorted_strings:
    for char in g_str:
        target_i, target_j = find_nearest_character_position(char, current_i, current_j, positions)
        print(target_i, target_j)
        current_i, current_j = target_i, target_j
        operations += 1
        if operations >= 5000:
            break
    if operations >= 5000:
        break