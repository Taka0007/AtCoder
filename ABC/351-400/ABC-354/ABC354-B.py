# Problem link    : https://atcoder.jp/contests/abc354/tasks/abc354_b
# Submission link : https://atcoder.jp/contests/abc354/submissions/53710954

# input
N = int(input())
user_name = []
user_rate = []
for _ in range(N):
    a,b = map(str,input().split())
    user_name.append(a)
    user_rate.append(int(b))
# sort username
user_name.sort()
# output
ans_index = sum(user_rate) % N
ans = user_name[ans_index]
print(ans)
