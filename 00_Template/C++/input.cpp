#include <iostream>
#include <unordered_set>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

int main() {
    // 文字列を1つ入力
    string S;
    cin >> S;

    // 整数を1つ入力
    int a;
    cin >> a;

    // 小数を1つ入力
    double af;
    cin >> af;

    // 整数を2つ入力
    int b, c;
    cin >> b >> c;

    // 整数をリスト形式で入力
    int n;
    cin >> n;
    vector<int> num_list(n);
    for (int i = 0; i < n; ++i) {
        cin >> num_list[i];
    }

    return 0;
}

