# Problem link    : https://atcoder.jp/contests/abc344/tasks/abc344_a
# Submission link : https://atcoder.jp/contests/abc344/submissions/51028304

# input
S = input()
ans = ''
delete = False
for i in range(len(S)):
    if delete:
        if S[i]=='|':
            delete = False
    else:
        if S[i]=='|':
            delete = True
        else:
            ans += S[i]
# output
print(ans)