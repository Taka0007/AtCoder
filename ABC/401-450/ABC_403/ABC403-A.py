# Problem link    : http://atcoder.jp/contests/abc403/tasks/abc403_a
# Submission link : https://atcoder.jp/contests/abc403/submissions/65303695

# input
N = int(input())
A = list(map(int,input().split()))
# calc
ans = 0
for i in range(N):
    if (i+1)%2==1:
        ans += A[i]
# output
print(ans)
