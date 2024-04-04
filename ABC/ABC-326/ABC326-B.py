# Problem link    : https://atcoder.jp/contests/abc326/tasks/abc326_b
# Submission link : https://atcoder.jp/contests/abc326/submissions/52000932

# input
N = int(input())
max_num = 10**7
# output
for i in range(N,max_num):
    if int(str(i)[0])*int(str(i)[1]) == int(str(i)[2]):
        print(i)
        break