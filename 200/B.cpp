#include<bits/stdc++.h>
#include<iostream>
#include<math.h>

using namespace std;

int main(){
               int64_t N,k;  cin>>N>>k;

               int s=0; 

               while(s<k)
               {if(N%200==0){N=N/200;}

               else{N=(N*10+2)*100;}
               
               s++;
               }

               cout<<N<<endl;
               }
