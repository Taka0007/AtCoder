# Problem link    : https://atcoder.jp/contests/abc340/tasks/abc340_a
# Submission link : https://atcoder.jp/contests/abc340/submissions/51426072

# input
A,B,D = map(int,input().split())
ans = [A]
# calculation
while ans[-1] + D <= B:
    num = ans[-1] + D
    ans.append(num)
# output
print(*ans)