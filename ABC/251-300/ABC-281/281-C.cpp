#include<iostream>
#include<math.h>
#include<algorithm>
#include<random>
#include<vector>
using namespace std;
int main(){
    
    long long N,T;
    cin>>N>>T;
    
    vector<long long> A(N);
    
    for(long long i=0; i<N; ++i){
        cin>>A[i];
    }
    
    
    long long sum = 0;
    for(long long i=0; i<N; ++i){
        sum += A[i];
    }
    

    long long newT = T%sum;
    
    for(long long i=0; i<N; ++i){
        newT -= A[i];
        
        if(newT <= 0){
            cout<<i+1<<' '<<A[i] - abs(newT)<<endl;
            break;
        } 
    }
    
}
