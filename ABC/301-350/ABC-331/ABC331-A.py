# input
M,D = map(int,input().split())
y,m,d = map(int,input().split())

## ans variables
ansY = y
ansM = m
ansD = d

if d == D:
    ansD = 1
    ansM += 1
    if ansM > M:
        ansM = 1
        ansY += 1
else:
    ansD += 1

# output
print(ansY,ansM,ansD,sep=" ")