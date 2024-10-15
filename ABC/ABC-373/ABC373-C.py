# Problem link    : https://atcoder.jp/contests/abc373/tasks/abc373_c
# Submission link : https://atcoder.jp/contests/abc373/submissions/58841464

# input
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# calc
ans = max(A) + max(B)
# output
print(ans)
