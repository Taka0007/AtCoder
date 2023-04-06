N,X = map(int,input().split())
num = list(map(int,input().split()))
ans = 'No'

#数字のsetを作る
number = set(num)

for i in range(N):
    if num[i]+X in number:
        ans = 'Yes'
print(ans)
