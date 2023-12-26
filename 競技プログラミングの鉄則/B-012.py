# Problem: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck
# Submit : https://atcoder.jp/contests/tessoku-book/submissions/48859558

# input
N = int(input())

# compute
left  = 0
right = N
ans   = (left + right) / 2
error = (ans**3 + ans) - N 

while abs(error) > 10**(-4):
    if error > 0:
        right = ans
    else:
        left = ans
    ans = (left + right) / 2
    error = (ans**3 + ans) - N

# output
print(ans)