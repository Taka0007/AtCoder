num = list(map(int,input().split()))
now = num[0]
flag1 = True
flag2 = True
flag3 = True

for i in range(1,8):
    if now > num[i]:
        flag1 = False
        break
    now = num[i]
    
if min(num)<100 or max(num)>675:
    flag2 = False

for i in range(8):
    if num[i]%25 != 0:
        flag3 = False
        break

if flag1 and flag2 and flag3:
    print('Yes')
else:
    print('No')