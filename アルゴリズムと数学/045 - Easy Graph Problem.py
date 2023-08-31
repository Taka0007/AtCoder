N,M = map(int,input().split())
graph = {i: set() for i in range(1, N + 1)}
num = []
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    num.append((a, b))

for a, b in num:
    graph[a].add(b)
    graph[b].add(a)

for i in graph:
    min_num = 0
    for j in graph[i]:
        if j < i:
            min_num += 1
    if min_num==1:
        ans += 1
print(ans)