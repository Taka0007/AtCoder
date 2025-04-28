# Problem link    : https://atcoder.jp/contests/abc362/tasks/abc362_a
# Submission link : https://atcoder.jp/contests/abc362/submissions/55587835

# input
price_lis = list(map(int,input().split()))
C = input()
# output
if C == 'Red':
    ans = min(price_lis[1],price_lis[2])
elif C == 'Green':
    ans = min(price_lis[0],price_lis[2])
else:
    ans = min(price_lis[0],price_lis[1])
print(ans)
