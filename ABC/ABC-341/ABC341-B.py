# Problem link    : https://atcoder.jp/contests/abc341/tasks/abc341_b
# Submission link : https://atcoder.jp/contests/abc341/submissions/50346969

# input
N = int(input())
A = list(map(int,input().split()))
S = []
T = []
for _ in range(N-1):
    s,t = map(int,input().split())
    S.append(s)
    T.append(t)

for i in range(N-1):
    if A[i] >= S[i]:
        A[i+1] += (A[i]//S[i])*T[i]
# output        
print(A[-1])