N = int(input())
D = list(map(int,input().split()))
ans = 0

# ゾロ目の数を数える
def is_OK(a,b):
    num = []

    if a >= 10:
        num.append(a//10)
        num.append(a%10)
    else:
        num.append(a)
    
    if b >= 10:
        num.append(b//10)
        num.append(b%10)
    else:
        num.append(b)
    
    if len(set(num))==1:
        return True
    else:
        return False


for i in range(1,N+1):
    for j in range(1,D[i-1]+1):
        if is_OK(i,j):
            ans += 1

print(ans)