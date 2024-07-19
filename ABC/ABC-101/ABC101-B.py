# Problem link    : https://atcoder.jp/contests/abc101/tasks/abc101_b
# Submission link : https://atcoder.jp/contests/abc101/submissions/55730893

# input
N = input()
# calc ans
S_N = 0
for i in range(len(N)):
    S_N += int(N[i])
# output
if int(N) % S_N == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)