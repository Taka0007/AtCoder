# Problem link: https://atcoder.jp/contests/apc001/tasks/apc001_a
# Submission link: https://atcoder.jp/contests/apc001/submissions/52759978

# input
X,Y = map(int,input().split())
# cal ans
ans = X
if X % Y == 0:
    ans = -1
else:
    while ans < 10**18 + 1:
        if ans % Y != 0:
            break
        ans += X
# output
print(ans)