N = int(input())

if N>= -2**31 and N<=2**31:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)