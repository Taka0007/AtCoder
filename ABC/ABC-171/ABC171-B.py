# Problem link    : https://atcoder.jp/contests/abc171/tasks/abc171_b
# Submission link : https://atcoder.jp/contests/abc171/submissions/50956441

# input
N,K = map(int,input().split())
P = list(map(int,input().split()))

# output
P.sort()
ans = 0
for i in range(K):
    ans += P[i]
print(ans)