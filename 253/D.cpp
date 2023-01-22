#define _GLIBCXX_DEBUG
#include<bits/stdc++.h>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<random>
using namespace std;
int GCD(long long m, long long n) //最大公約数
{
  if(n==0){return m;}
  else{return GCD(n,m%n);}
}


int main(){

long long N,A,B;
cin>>N>>A>>B;
unsigned long long ans;

long long GCD_AB = GCD(A,B); //最大公約数
long long K = GCD_AB*(A/GCD_AB)*(B/GCD_AB); //最小公倍数

long long num_A = N/A;
long long num_B = N/B;
long long num_AB = N/K;

unsigned long long allsum = (N*(N+1))/2;
unsigned long long A_sum = ((num_A*(num_A+1))/2)*A;
unsigned long long B_sum = ((num_B*(num_B+1))/2)*B;
unsigned long long AB_sum = ((num_AB*(num_AB+1))/2)*K;

ans = allsum - A_sum -B_sum +AB_sum;

cout<<ans<<endl;

return 0;

}
