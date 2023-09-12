# O(N^2)解法
N      = int(input())
points = []
ans = 10**10

def distance(x1,y1,x2,y2):
    preans = (x1-x2)**2 + (y1-y2)**2
    return (preans)**(1/2)

for i in range(N):
    x,y = map(int,input().split())
    points.append([x,y])
    
for i in range(N):
    for j in range(i+1,N):
        dis = distance( points[i][0], points[i][1], points[j][0], points[j][1])
        ans = min(ans, dis)
print(ans)