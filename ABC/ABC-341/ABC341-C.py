# Problem link    : https://atcoder.jp/contests/abc341/tasks/abc341_c
# Submission link : https://atcoder.jp/contests/abc341/submissions/50383786

# input
H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue

        x, y = i, j
        flag = True
        for k in range(N):
            if T[k] == 'L':
                y -= 1
            elif T[k] == 'R':
                y += 1
            elif T[k] == 'U':
                x -= 1
            elif T[k] == 'D':
                x += 1

            if x < 0 or x >= H or y < 0 or y >= W or S[x][y] == '#':
                flag = False
                break

        if flag:
            ans += 1
# output
print(ans)