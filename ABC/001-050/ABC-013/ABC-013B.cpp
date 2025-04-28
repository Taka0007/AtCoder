#include <iostream>
using namespace std;
int main(void){
    
    int a;
    int b;
    cin>>a;
    cin>>b;
  	int ans;
    
    ans = min(abs(a-b), abs(min(a,b)+10-max(a,b)));
    cout<<ans<<endl;
}
