#include <iostream>
#include <unordered_set>
#include <vector>
#include<math.h>
using namespace std;
int main() {
    string S;
    cin >> S;
    
    string correct_str = "CODEFESTIVAL2016";
    int ans = 0;
    
    for(int i=0; i<S.length(); i++){
        if(S[i]!=correct_str[i]){
            ans++;
        }
    }
    
    cout << ans << endl;
    return 0;
}