# Problem link    : https://atcoder.jp/contests/abc373/tasks/abc373_a
# Submission link : https://atcoder.jp/contests/abc373/submissions/60390336

# input & prosess
ans = 0
for i in range(1,13):
    S = input()
    if len(S) == i:
        ans += 1
# output
print(ans)
