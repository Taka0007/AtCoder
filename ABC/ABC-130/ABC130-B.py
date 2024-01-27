# Pronlem: https://atcoder.jp/contests/abc130/tasks/abc130_b
# Submission:

# input
N,X = map(int,input().split())
L   = list(map(int,input().split()))

# declare ans val
ans = 1
dis = 0

# simulation
for i in range(N+2):
    try:
        dis += L[i]
    except:
        break
    if dis > X:
        break
    ans += 1

# output
print(ans)