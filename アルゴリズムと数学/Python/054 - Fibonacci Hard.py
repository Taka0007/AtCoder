import numpy as np

def dot(A1, A2, N, mod):
    # N: 行列のサイズ
    A = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                A[i][j] = (A[i][j] + (A1[i][k] * A2[k][j]) % mod) % mod
    return A

def pow_mat(A, K, N, mod):
    # A: 累乗する行列, k: 累乗数, n: 行列Aのサイズ
    P = np.eye(N, dtype=int)
    while K:
        if K & 1:
            P = dot(P, A, N, mod)
        A = dot(A, A, N, mod)
        K >>= 1
    return P

N = int(input())
mat = np.array([[1, 1], [1, 0]], dtype=int)
mod = 10**9
ans_matrix = pow_mat(mat, N-1, 2, mod)
ans = (ans_matrix[1][0] + ans_matrix[1][1]) % mod
print(ans)