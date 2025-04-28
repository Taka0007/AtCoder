#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

int main() {
   
   int a,b;
   cin >> a >> b;
    string ans;

   if(b/2==a){
    ans = "Yes";
   }
    else{
        ans = "No";
    }

    cout << ans << endl;
   
    return 0;
}