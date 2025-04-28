# Problem link    : https://atcoder.jp/contests/abc343/tasks/abc343_b
# Submission link : https://atcoder.jp/contests/abc343/submissions/51230860

# input
N = int(input())
# output
for i in range(N):
    ans_list = []
    num = list(map(int, input().split()))
    for j in range(N):
        if num[j]==1:
            ans_list.append(j+1)
    print(*ans_list)