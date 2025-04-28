N = int(input())
A = list(map(int,input().split()))
ans = 0

for i in range(N):
    while True:
        if A[i]%3==2:
            ans  += 1
            A[i] -= 1
        if A[i]%2==0:
            ans  += 1
            A[i] -= 1
        else:
            break
print(ans)