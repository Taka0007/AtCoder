# Problem link    : https://atcoder.jp/contests/abc344/tasks/abc344_b
# Submission link : https://atcoder.jp/contests/abc344/submissions/51035339

# input
num = []
while True:
    a = int(input())
    num.append(a)
    
    if a==0:
        break
# output
num.reverse()
for nu in num:
    print(nu)