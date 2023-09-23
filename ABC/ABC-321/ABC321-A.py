N = int(input())

if N<=9:
    flag = True
else:
    str_N = str(N)
    flag = True
    for i in range(len(str_N)-1):
        if str_N[i] <= str_N[i+1]:
            flag = False
            break
if flag:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)