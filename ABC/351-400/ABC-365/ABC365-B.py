# Problem link    : https://atcoder.jp/contests/abc365/tasks/abc365_b
# Submission link : https://atcoder.jp/contests/abc365/submissions/56256150

# input
N = int(input())
A = list(map(int,input().split()))
# make a sorted list of A
sort_A = sorted(A)
next_max = sort_A[-2]
ans = A.index(next_max) + 1
# output
print(ans)
