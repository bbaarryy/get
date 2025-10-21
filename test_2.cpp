#include <fstream>
#include <iostream> 
#include <algorithm>
#include <vector>
#include <map>
#include <chrono>
#include <ctime>
#include <random>

using namespace std;

#define ll long long
#define REP(n) for(int i = 0 ; i < n ; i ++)

struct duo{
    ll n;
    string s;
};

ll bin_pow(ll a,ll n){//a^n
    if(n==1){return a;}

    else{
        if(n%2==0){
            ll j = n/2;
            ll b = bin_pow(a,j);//a^(n/2)
            return b*b;
        }
        else{
            ll j=n-1;
            return a * bin_pow(a,j);
        }
    }
}

int main(){
    cout << bin_pow(5,10);
}