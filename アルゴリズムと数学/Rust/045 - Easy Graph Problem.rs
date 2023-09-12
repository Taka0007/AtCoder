use std::collections::HashSet;
use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().expect("Invalid input");
    let m: usize = iter.next().unwrap().parse().expect("Invalid input");

    let mut graph = vec![HashSet::new(); n + 1];
    let mut num = Vec::new();
    let mut ans = 0;

    for _ in 0..m {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().expect("Invalid input");
        let b: usize = iter.next().unwrap().parse().expect("Invalid input");
        num.push((a, b));
    }

    for (a, b) in &num {
        graph[*a].insert(*b);
        graph[*b].insert(*a);
    }

    for i in 1..=n {
        let mut min_num = 0;
        for &j in &graph[i] {
            if j < i {
                min_num += 1;
            }
        }
        if min_num == 1 {
            ans += 1;
        }
    }

    println!("{}", ans);
}