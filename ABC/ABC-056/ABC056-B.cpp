#include <iostream>
#include <unordered_set>
#include <vector>
#include<math.h>
using namespace std;

int main() {
    int w,a,b;
    cin >> w >> a >> b;
    int ans;
    
    if( (b+w>=a && b+w<=a+w) || (a<=b && b<=a+w) ){
        ans = 0;
    }
    else{
     ans = min( abs(a-b-w), abs(b-a-w));   
    }
    cout << ans << endl;
    return 0;
}