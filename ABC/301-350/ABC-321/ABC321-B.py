N,X = map(int,input().split())
A   = list(map(int,input().split()))

# 諦めて全探索
ans = -1

# 得点(0-100)を全探索する
for i in range(101):
    # iを追加する
    A.append(i)
    A.sort()
    if sum(A)-A[0]-A[N-1] >= X:
        ans = i
        break
    A.remove(i)
print(ans)