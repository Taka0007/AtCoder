# Problem link    : https://atcoder.jp/contests/arc007/tasks/arc007_1
# Submission link : https://atcoder.jp/contests/arc007/submissions/53535023

# input
break_num = input()
S = input()
ans = ''
# output
for st in S:
    if st != break_num:
        ans += st
print(ans)
