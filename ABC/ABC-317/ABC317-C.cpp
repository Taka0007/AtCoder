#include <iostream>
#include <vector>

class Edge {
public:
    int start, end, leng;
    Edge(int start, int end, int leng) : start(start), end(end), leng(leng) {}
};

int dfs(int node, std::vector<bool>& visited, std::vector<std::vector<Edge>>& graph) {
    visited[node] = true;
    int max_length = 0;
    
    for (const Edge& edge : graph[node]) {
        if (!visited[edge.end]) {
            max_length = std::max(max_length, edge.leng + dfs(edge.end, visited, graph));
        }
    }
    
    visited[node] = false;
    return max_length;
}

const int INF = 1e9;

int main() {
    int N, M;
    std::cin >> N >> M;
    
    std::vector<std::vector<Edge>> graph(N);
    for (int i = 0; i < M; ++i) {
        int u, v, w;
        std::cin >> u >> v >> w;
        graph[u - 1].emplace_back(u - 1, v - 1, w);
        graph[v - 1].emplace_back(v - 1, u - 1, w);
    }

    int max_length = 0;
    for (int i = 0; i < N; ++i) {
        std::vector<bool> visited(N, false);
        max_length = std::max(max_length, dfs(i, visited, graph));
    }

    std::cout << max_length << std::endl;
    
    return 0;
}