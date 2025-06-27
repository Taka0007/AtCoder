use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    // 文字列を1つ入力
    let s = lines.next().unwrap().unwrap();

    // 整数を1つ入力
    let a: i32 = lines.next().unwrap().unwrap().trim().parse().unwrap();

    // 小数を1つ入力
    let af: f64 = lines.next().unwrap().unwrap().trim().parse().unwrap();

    // 整数を2つ入力
    let bc: Vec<i32> = lines.next().unwrap().unwrap().split_whitespace()
                              .map(|x| x.parse().unwrap()).collect();
    let (b, c) = (bc[0], bc[1]);

    // 整数をリスト形式で入力
    let num_list: Vec<i32> = lines.next().unwrap().unwrap().split_whitespace()
                                  .map(|x| x.parse().unwrap()).collect();

    println!("{:?} {} {} {} {} {:?}", s, a, af, b, c, num_list);
}