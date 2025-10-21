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

struct trio{
    ll a,b,c;
};

int main(){
    ll n,m;
    cin >> n >> m;

    vector<vector<ll>> arr(n,vector<ll> (m,0));

    for(int i = 0 ; i < n ; i ++){
        for(int j = 0 ; j < m ; j ++){
            cin >> arr[i][j];
        }
    }

    vector<vector<ll>> dp(n,vector<ll> (m,0));
    vector<vector<string>> dir(n,vector<string> (m,""));
    dp[0][0] = arr[0][0];

    for(int i = 1 ; i < m;i++){
        dp[0][i] = dp[0][i-1] + arr[0][i];
        
    }

    for(int i = 1 ; i < n;i++){
        dp[i][0] = dp[i-1][0] + arr[i][0];
    }

    for(int i = 1 ; i < n ; i++){
        for(int j = 1 ; j < m ; j ++){
            if(dp[i-1][j] <= dp[i][j-1]){
                dp[i][j] = dp[i][j-1] + arr[i][j];
                dir[i][j] = "right";
            }
            else{
                dp[i][j] = dp[i-1][j] + arr[i][j];
                dir[i][j] = "down";
            }   
        }
    }

    ll i =n-1;ll j=m-1;
    vector<string> ans;
    while(i != 1 || j!= 1){
        ans.push_back(dir[i][j]);
        if(dir[i][j] == "down"){ i--;}
        else{j--;}
    }
    REP(ans.size()){
        cout << ans[i] << '\n';
    }
}