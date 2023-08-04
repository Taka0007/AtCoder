N,M = map(int,input().split())
graph = {i: set() for i in range(1, N + 1)}
num = []
for i in range(M):
    a, b = map(int, input().split())
    num.append((a, b))

for a, b in num:
    graph[a].add(b)
    graph[b].add(a)
print(graph)
print(graph[1])