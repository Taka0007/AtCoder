import sys
import numpy as np
import random
import time
from collections import Counter, defaultdict
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern

# 文字列の出現回数評価（モンテカルロシミュレーション）
def evaluate(S, P, state_chars, transition_matrix, trials=500):
    M = len(state_chars)
    score = 0
    state_to_char = {i: c for i, c in enumerate(state_chars)}
    
    for _ in range(trials):
        s = state_to_char[0]
        current_state = 0
        for _ in range(1, 50):
            probs = transition_matrix[current_state]
            current_state = np.random.choice(range(M), p=np.array(probs)/100)
            s += state_to_char[current_state]
        
        for si, pi in zip(S, P):
            if si in s:
                score += pi

    return score / trials

# 状態遷移生成
def random_transition(M):
    matrix = []
    for _ in range(M):
        probs = np.random.dirichlet(np.ones(M)) * 100
        matrix.append(probs)
    return matrix

# メイン関数
def main():
    start_time = time.time()

    N, M, L = map(int, sys.stdin.readline().split())
    S, P = [], []
    chars = ''
    for _ in range(N):
        s, p = sys.stdin.readline().split()
        S.append(s)
        P.append(int(p))
        chars += s

    char_freq = Counter(chars)
    most_common_chars = [char for char, _ in char_freq.most_common()]
    state_chars = [most_common_chars[i % len(most_common_chars)] for i in range(M)]

    X, y = [], []
    best_score, best_matrix = -1, None

    # 初期ランダムサンプリング
    for _ in range(15):
        transition_matrix = random_transition(M)
        score = evaluate(S, P, state_chars, transition_matrix)
        X.append(np.array(transition_matrix).flatten())
        y.append(score)
        if score > best_score:
            best_score = score
            best_matrix = transition_matrix

    # GPモデル
    gp = GaussianProcessRegressor(kernel=Matern(nu=2.5), alpha=1e-6)

    while time.time() - start_time < 1.8:
        gp.fit(X, y)

        # 次の候補を生成（獲得関数は簡易ランダムサンプリング）
        candidates = [random_transition(M) for _ in range(5)]
        candidate_scores = gp.predict(np.array([np.array(c).flatten() for c in candidates]))
        best_candidate_idx = np.argmax(candidate_scores)

        transition_matrix = candidates[best_candidate_idx]
        score = evaluate(S, P, state_chars, transition_matrix)

        X.append(np.array(transition_matrix).flatten())
        y.append(score)

        if score > best_score:
            best_score = score
            best_matrix = transition_matrix

    # 結果の出力
    for i in range(M):
        probs = [int(round(p)) for p in best_matrix[i]]
        diff = 100 - sum(probs)
        probs[random.randint(0, M - 1)] += diff
        print(state_chars[i], *probs)

if __name__ == "__main__":
    main()
