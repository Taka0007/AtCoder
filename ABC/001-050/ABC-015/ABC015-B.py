# Problem link    : https://atcoder.jp/contests/abc015/tasks/abc015_2
# Submission link : https://atcoder.jp/contests/abc015/submissions/51230995

# import
import math

# input
N = int(input())
A = list(map(int, input().split()))

# culculate
bug_count = 0
for i in range(N):
    if A[i] != 0:
        bug_count += 1
# output
ans = math.ceil(sum(A) / bug_count)
print(ans)