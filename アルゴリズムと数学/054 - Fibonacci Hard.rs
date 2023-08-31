use std::io;

fn multiply_matrix(a: [[i64; 2]; 2], b: [[i64; 2]; 2], modulo: i64) -> [[i64; 2]; 2] {
    let mut result = [[0; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            for k in 0..2 {
                result[i][j] = (result[i][j] + (a[i][k] * b[k][j]) % modulo) % modulo;
            }
        }
    }
    result
}

fn power_matrix(base: [[i64; 2]; 2], exponent: usize, modulo: i64) -> [[i64; 2]; 2] {
    if exponent == 0 {
        return [[1, 0], [0, 1]];
    }
    if exponent == 1 {
        return base;
    }
    let mut result = [[1, 0], [0, 1]];
    let mut current_power = base;
    let mut remaining_exponent = exponent;
    while remaining_exponent > 0 {
        if remaining_exponent % 2 == 1 {
            result = multiply_matrix(result, current_power, modulo);
        }
        current_power = multiply_matrix(current_power, current_power, modulo);
        remaining_exponent /= 2;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: usize = input.trim().parse().expect("Invalid input");
    
    let base_matrix = [[1, 1], [1, 0]];
    let modulo: i64 = 1_000_000_000;
    
    let ans_matrix = power_matrix(base_matrix, n - 1, modulo);
    let ans = (ans_matrix[1][0] + ans_matrix[1][1]) % modulo;
    println!("{}", ans);
}