N = int(input())
num = []
pi = 3.1415926535

for i in range(N):
    a = int(input())
    num.append(a)
num.sort()

ans = 0
for i in range(N-1,-1,-1):
    if i%2==1:
        ans -= (num[i]**2)*pi
    else:
        ans += (num[i]**2)*pi

print(abs(ans))