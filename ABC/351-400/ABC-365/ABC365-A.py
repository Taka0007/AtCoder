# Problem link    : https://atcoder.jp/contests/abc365/tasks/abc365_a
# Submission link : https://atcoder.jp/contests/abc365/submissions/56248554

# input
Y = int(input())
# calc ans
if Y % 4 != 0:
    ans = 365
elif Y % 100 != 0:
    ans = 366
elif Y % 400 == 0:
    ans = 366
else:
    ans = 365
# output
print(ans)
