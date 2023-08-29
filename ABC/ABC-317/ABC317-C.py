# 普通のpythonでは通らないので注意
# (PyPyなら通る)

class Edge:
    def __init__(self, start, end, leng):
        self.start = start
        self.end = end
        self.leng = leng

def dfs(node, visited, graph):
    visited[node] = True
    max_length = 0
    
    for edge in graph[node]:
        if not visited[edge.end]:
            max_length = max(max_length, edge.leng + dfs(edge.end, visited, graph))
    
    visited[node] = False
    return max_length

INF = 10**9 

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append(Edge(u - 1, v - 1, w))
    graph[v - 1].append(Edge(v - 1, u - 1, w))

max_length = 0
for i in range(N):
    visited = [False] * N
    max_length = max(max_length, dfs(i, visited, graph))

print(max_length)