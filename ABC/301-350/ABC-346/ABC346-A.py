# Problem link    : https://atcoder.jp/contests/abc346/tasks/abc346_a
# Submission link : https://atcoder.jp/contests/abc346/submissions/51615331

# input
N = int(input())
A = list(map(int,input().split()))
B = []
# calculation
for i in range(N-1):
    num = A[i] * A[i+1]
    B.append(num)
# output
print(*B)