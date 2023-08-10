use std::collections::{HashSet, HashMap};
use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().expect("Invalid input");
    let m: usize = iter.next().unwrap().parse().expect("Invalid input");

    let mut graph: HashMap<usize, HashSet<usize>> = HashMap::new();
    for i in 1..=n {
        graph.insert(i, HashSet::new());
    }

    let mut num: Vec<(usize, usize)> = Vec::new();
    for _ in 0..m {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().expect("Invalid input");
        let b: usize = iter.next().unwrap().parse().expect("Invalid input");
        num.push((a, b));
    }

    for (a, b) in num.iter() {
        graph.get_mut(a).unwrap().insert(*b);
        graph.get_mut(b).unwrap().insert(*a);
    }

    for i in 1..=n {
        println!("{}", friends_of_friends(i, &graph));
    }
}

fn friends_of_friends(id: usize, graph: &HashMap<usize, HashSet<usize>>) -> usize {
    let mut friends_list: HashSet<usize> = HashSet::new();
    let mut friends_of_friends_list: HashSet<usize> = HashSet::new();

    if let Some(friends) = graph.get(&id) {
        for &friend in friends {
            friends_list.insert(friend);
        }

        for &friend in friends_list.iter() {
            if let Some(friends_of_friend) = graph.get(&friend) {
                for &friend_of_friend in friends_of_friend {
                    if friend_of_friend != id && !friends_list.contains(&friend_of_friend) {
                        friends_of_friends_list.insert(friend_of_friend);
                    }
                }
            }
        }
    }

    friends_of_friends_list.len()
}