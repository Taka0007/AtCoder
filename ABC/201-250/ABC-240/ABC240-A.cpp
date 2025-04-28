#include <iostream>
#include <unordered_set>
#include <vector>
#include<math.h>
using namespace std;

int main() {
    int A,B;
    string ans;
    cin >> A >> B;

    if(abs(A-B)==1 || abs(A-B)==9){
        ans = "Yes";
    }
    else{
        ans = "No";
    }

    cout << ans << endl;

    return 0;
}