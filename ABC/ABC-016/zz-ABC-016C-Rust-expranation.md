```
use std::collections::{HashSet, HashMap};
use std::io;
```

std::collections::{HashSet, HashMap}: std::collectionsモジュールからHashSetとHashMapを使用するための指示です。これらはハッシュセットとハッシュマップを提供します。
std::io: 標準入出力を管理するioモジュールです。

```
fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().expect("Invalid input");
    let m: usize = iter.next().unwrap().parse().expect("Invalid input");
```
fn main() { ... }: Rustのエントリーポイントで、プログラムの実行がここから始まります。
let mut input = String::new();: 文字列型の可変変数inputを宣言し、新しい空の文字列を作成します。
io::stdin().read_line(&mut input).expect("Failed to read input");: 標準入力から1行読み取り、それをinputに格納します。expectは、エラーが発生した場合にエラーメッセージを表示します。
let mut iter = input.split_whitespace();: スペースで区切られた単語に分割するためのイテレータiterを作成します。
let n: usize = iter.next().unwrap().parse().expect("Invalid input");: イテレータから次の単語を取得し、文字列から整数に変換します。この行でユーザからの入力で得られた値が、変数nに整数型として格納されます。
同様にして、変数mも取得します。

```
    let mut graph: HashMap<usize, HashSet<usize>> = HashMap::new();
    for i in 1..=n {
        graph.insert(i, HashSet::new());
    }
```
HashMap<usize, HashSet<usize>>: キーがusize型で値がHashSet<usize>型のハッシュマップを宣言します。これは各ユーザの友達関係を表します。
for i in 1..=n { ... }: 1からnまでの範囲でループを実行し、各ユーザのIDをiに設定します。
graph.insert(i, HashSet::new());: graphにユーザIDをキーとして友達の集合を空のHashSetとして追加します。

```
    let mut num: Vec<(usize, usize)> = Vec::new();
    for _ in 0..m {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().expect("Invalid input");
        let b: usize = iter.next().unwrap().parse().expect("Invalid input");
        num.push((a, b));
    }
```
let mut num: Vec<(usize, usize)> = Vec::new();: (usize, usize)型のタプルを要素とするベクターnumを宣言します。友達関係の情報を保持します。
for _ in 0..m { ... }: 友達関係の数（m回）だけループを実行します。
let a: usize = iter.next().unwrap().parse().expect("Invalid input");: イテレータから次の単語を取得し、文字列から整数に変換して変数aに格納します。
同様に、変数bも取得し、タプル(a, b)をベクターnumに追加します。


```
    for (a, b) in num.iter() {
        graph.get_mut(a).unwrap().insert(*b);
        graph.get_mut(b).unwrap().insert(*a);
    }
```
for (a, b) in num.iter() { ... }: numベクターの各要素を(a, b)というタプルに展開してループを実行します。
graph.get_mut(a).unwrap().insert(*b);: aのユーザの友達リストにbを追加します。get_mutは、ユーザIDをキーにして友達リストを取得し、unwrapはエラーチェックを省略しています。
同様に、bのユーザの友達リストにもaを追加します。
