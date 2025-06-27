# Problem link    : https://atcoder.jp/contests/abc365/tasks/abc365_c
# Submission link : https://atcoder.jp/contests/abc365/submissions/56304265

# input
N, M = map(int, input().split())
A = list(map(int, input().split()))

# judge whether host can pay K
def judge_grant(K):
    payment = 0
    for i in range(N):
        payment += min(A[i], K)
    return payment <= M

# calc ans
left  = 0
right = max(A) + 1

while left < right:
    mid = (left + right) // 2
    if judge_grant(mid):
        left = mid + 1
    else:
        right = mid

# output
max_possible_K = left - 1
if max_possible_K == max(A):
    print('infinite')
else:
    print(max_possible_K)
