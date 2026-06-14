# Problem link    : https://atcoder.jp/contests/abc072/tasks/abc072_b
# Submission link : https://atcoder.jp/contests/abc072/submissions/76679561

# input
s = input()
# make ans
ans = ""
for i in range(len(s)):
    if i%2==0:
        ans += s[i]
# output
print(ans)
