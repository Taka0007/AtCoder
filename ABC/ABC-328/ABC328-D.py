# Problem link: https://atcoder.jp/contests/abc328/tasks/abc328_d
# Submit link: 

# import
from collections import deque

# input
S = input()

# 空のキューを作成
que = deque()

# 左から順番にキューに追加
for num in range(len(S)):
    que.append(S[num])