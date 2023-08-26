N,H,X = map(int,input().split())
P = list(map(int,input().split()))
goal = X - H

for i in range(N):
    if P[i] >= goal:
        print(i+1)
        break