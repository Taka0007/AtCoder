# Problem link    : https://atcoder.jp/contests/abc408/tasks/abc408_c
# Submission link : https://atcoder.jp/contests/abc408/submissions/69435869

# input
N,M = map(int,input().split())
# calc cumsum
cumsum = [0] * N
data   = [0] * N 
for _ in range(M):
    l,r = map(int,input().split())
    data[l-1] += 1
    if r < N:
        data[r] -= 1

cumsum[0] = data[0]
for i in range(1,N):
    cumsum[i] = cumsum[i-1] + data[i]
# output answer
ans = min(cumsum)
print(ans)
