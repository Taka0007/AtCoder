# Problem Link    : https://atcoder.jp/contests/arc057/tasks/arc057_a
# Submission Link : https://atcoder.jp/contests/arc057/submissions/48882925

# input
A,K = map(int,input().split())

# declare variables
limit = 2*(10**12)
day   = 0

# operate
while A < limit:
    A += 1 + K*A
    day += 1

# output
print(day)