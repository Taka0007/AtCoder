#define _GLIBCXX_DEBUG
#include<bits/stdc++.h>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<random>
using namespace std;
int main(){
int A,B,C,D,E,F;
cin>>A>>B>>C>>D>>E>>F;

vector<int> Aa(6);
Aa={A,B,C,D,E,F};

sort(Aa.begin(),Aa.end());
reverse(Aa.begin(),Aa.end());

int answer=Aa[2];
cout<<answer<<endl;
return 0;
}
