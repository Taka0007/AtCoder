use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let values: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let h1 = values[0];
    let h2 = values[1];

    let mut ans = h1 - h2;
    
    println!("{}", ans);
}