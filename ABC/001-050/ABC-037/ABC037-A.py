# Problem link    : https://atcoder.jp/contests/abc037/tasks/abc037_a
# Submission link : https://atcoder.jp/contests/abc037/submissions/52478393

# input
A,B,C = map(int,input().split())
# answer
ans = C // min(A,B)
# output
print(ans)