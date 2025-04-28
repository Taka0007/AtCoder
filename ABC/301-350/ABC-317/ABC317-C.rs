use std::io;

#[derive(Clone)]  // Clone トレイトを手動で実装
struct Edge {
    start: usize,
    end: usize,
    leng: i32,
}

impl Edge {
    fn new(start: usize, end: usize, leng: i32) -> Self {
        Edge { start, end, leng }
    }
}

fn dfs(node: usize, visited: &mut Vec<bool>, graph: &Vec<Vec<Edge>>) -> i32 {
    visited[node] = true;
    let mut max_length = 0;
    
    for edge in &graph[node] {
        if !visited[edge.end] {
            max_length = std::cmp::max(max_length, edge.leng + dfs(edge.end, visited, graph));
        }
    }
    
    visited[node] = false;
    max_length
}

const INF: i32 = 1_000_000_000;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let N: usize = iter.next().unwrap().parse().unwrap();
    let M: usize = iter.next().unwrap().parse().unwrap();

    let mut graph: Vec<Vec<Edge>> = vec![vec![]; N];
    for _ in 0..M {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let u: usize = iter.next().unwrap().parse().unwrap();
        let v: usize = iter.next().unwrap().parse().unwrap();
        let w: i32 = iter.next().unwrap().parse().unwrap();
        graph[u - 1].push(Edge::new(u - 1, v - 1, w));
        graph[v - 1].push(Edge::new(v - 1, u - 1, w));
    }

    let mut max_length = 0;
    for i in 0..N {
        let mut visited = vec![false; N];
        max_length = std::cmp::max(max_length, dfs(i, &mut visited, &graph));
    }

    println!("{}", max_length);
}