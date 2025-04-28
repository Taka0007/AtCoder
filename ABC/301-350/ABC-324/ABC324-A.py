N = int(input())
A = list(map(int, input().split()))

if len(set(A))==1:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)