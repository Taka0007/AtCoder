X = int(input())

for i in range(1,int(X**(1/2)+1)):
    if i**2 <= X:
        ans = i**2

print(ans)