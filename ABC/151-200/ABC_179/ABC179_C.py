# Problem link    : https://atcoder.jp/contests/abc179/tasks/abc179_c
# Submission link : https://atcoder.jp/contests/abc179/submissions/60816028

# input
N = int(input())
# calc ans
ans = 0
for A in range(1,N):
    ans += (N-1)//A
# output
print(ans)
