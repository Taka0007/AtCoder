# import
# ---------
import random
# ---------

# input
# ---------
N,M = map(int,input().split())

# 初期状態の指の位置
s_i, s_j = map(int,input().split())

# キーボードの座標
A = [list(map(str,input().split())) for _ in range(N)]

# 縁起のいい文字列一覧
good_str = [input() for _ in range(N)]
# ---------

# raandom output
for _ in range(100):
    rand1 = random.randint(0, N - 1)
    rand2 = random.randint(0, N - 1)
    print(rand1, rand2)


# result
# ---------
sub1:
sub2:
# ---------