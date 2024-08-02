# Problem link    : https://atcoder.jp/contests/abc364/tasks/abc364_c
# Submission link : 

# input
N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

## solve about A
ans_a = N+1
A.sort()
A.reverse()
cumulative_sum_A = [0]*(N)
cumulative_sum_A[0] = A[0]
for i in range(1,N):
    cumulative_sum_A[i] = cumulative_sum_A[i-1] + A[i]


## solve about B




# output
ans = min(ans_a, ans_b)
print(ans)
