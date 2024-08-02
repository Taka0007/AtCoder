# Problem link    : https://atcoder.jp/contests/abc364/tasks/abc364_c
# Submission link : https://atcoder.jp/contests/abc364/submissions/56218489

# input
N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

## solve about A
ans_a = 0
sum_a = 0
A.sort()
A.reverse()
for i in range(N):
    sum_a += A[i]
    ans_a += 1
    if sum_a > X:
        break
## solve about B
ans_b = 0
sum_b = 0
B.sort()
B.reverse()
for i in range(N):
    sum_b += B[i]
    ans_b += 1
    if sum_b > Y:
        break
# output
ans = min(ans_a, ans_b)
print(ans)
