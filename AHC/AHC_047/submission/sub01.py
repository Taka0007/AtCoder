# import
import sys
import random
import time
from collections import Counter, defaultdict

def main():
    # 時間計測開始
    start_time = time.time()

    # input
    N, M, L = map(int, sys.stdin.readline().split())
    S, P = [], []
    chars = ''
    for _ in range(N):
        s, p = sys.stdin.readline().split()
        S.append(s)
        P.append(int(p))
        chars += s

    # 文字の頻度を計算
    char_freq = Counter(chars)
    most_common_chars = [char for char, _ in char_freq.most_common()]
    state_chars = [most_common_chars[i % len(most_common_chars)] for i in range(M)]

    # 文字列の重なりを計算
    overlaps = defaultdict(lambda: defaultdict(int))
    for s, p in zip(S, P):
        for i in range(len(s) - 1):
            overlaps[s[i]][s[i + 1]] += p

    # 状態遷移の初期化
    transition_matrix = []
    for i in range(M):
        current_char = state_chars[i]
        row = [0] * M
        total = 0
        for j in range(M):
            next_char = state_chars[j]
            weight = overlaps[current_char][next_char] + 1  # ゼロ除算防止
            row[j] = weight
            total += weight

        # パーセントに変換
        row = [max(1, round(100 * x / total)) for x in row]

        # 合計を100に調整
        diff = 100 - sum(row)
        idx = random.randint(0, M - 1)
        row[idx] += diff

        transition_matrix.append(row)

    # 時間制限を超えない範囲で遷移を少し調整
    while time.time() - start_time < 1.9:
        i = random.randint(0, M - 1)
        j1, j2 = random.sample(range(M), 2)
        if transition_matrix[i][j1] > 1:
            transition_matrix[i][j1] -= 1
            transition_matrix[i][j2] += 1

    # output
    for i in range(M):
        print(state_chars[i], *transition_matrix[i])

if __name__ == "__main__":
    main()
