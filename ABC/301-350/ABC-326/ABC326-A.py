x,y = map(int,input().split())

if y-x>0 and y-x<=2:
    ans = 'Yes'
elif y-x>0 and y-x>2:
    ans = 'No'
elif x-y>0 and abs(x-y)<=3:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)