# Problem link    : https://atcoder.jp/contests/abc367/tasks/abc367_b
# Submission link : https://atcoder.jp/contests/abc367/submissions/57354816

# input
X = str(input())
# delete last 0
while True:
    if X[-1] == '0':
        X = X.rstrip('0')
    elif X[-1] == '.':
        X = X.rstrip('.')
        break
    else:
        break
# output
print(X)
