N = input()

if len(N)<=3:
    print(N)
else:
    ans = list(N)
    for i in range(3,len(N)):
        ans[i] = '0'
    print(*ans,sep='')