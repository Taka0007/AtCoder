#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;

    vector<int> num(N);
    for (int i = 0; i < N; ++i) {
        cin >> num[i];
    }
    string ans = "No";

    // 数字のunordered_setを作る
    unordered_set<int> number(num.begin(), num.end());
    for (int i = 0; i < N; ++i) {
        if (number.find(num[i] + X) != number.end()) {
            ans = "Yes";
            break;
        }
    }
    cout << ans << endl;
    return 0;
}
