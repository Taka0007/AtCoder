# Problem link    : https://atcoder.jp/contests/abc344/tasks/abc344_c
# Submission link : https://atcoder.jp/contests/abc344/submissions/51044526

# input
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))

# Set of numbers that can be made
valid_sum = set()
for i in range(N):
    for j in range(M):
        for k in range(L):
            num = A[i] + B[j] + C[k]
            valid_sum.add(num)
            
# output
for l in range(Q):
    if X[l] in valid_sum:
        print('Yes')
    else:
        print('No')