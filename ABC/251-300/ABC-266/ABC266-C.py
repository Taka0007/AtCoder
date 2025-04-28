from scipy.spatial import ConvexHull
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
c1,c2 = map(int,input().split())
d1,d2 = map(int,input().split())

points = [ [a1,a2],[b1,b2], [c1,c2], [d1,d2] ]
hull = ConvexHull(points)
points = hull.points
hull_points = points[hull.vertices]

if len(hull_points)==4:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)