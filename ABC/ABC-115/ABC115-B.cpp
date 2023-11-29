#include <iostream>
#include <unordered_set>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

int main() {

    int N,ans;
    cin >> N;
    ans = 0;
    vector<int> price(N);
    for (int i = 0; i < N; i++) {
        cin >> price[i];
    }

    for (int i = 0; i < N; i++) {
        ans += price[i];
    }

    // 一番高いものを半額にする
    int maxPrice = *max_element(price.begin(), price.end());
    ans -= maxPrice / 2;
    cout << ans << endl;
   
    return 0;
}