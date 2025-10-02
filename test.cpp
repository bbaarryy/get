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

vector<int> merging(vector<int>& a,vector<int>& b){
    vector<int> ans;
    int l = 0,r=0;
    while(l < a.size() && r < b.size()){
        if(a[l] < b[r]){
            ans.push_back(a[l]);
            l++;
        }
        else{
            ans.push_back(b[r]);
            r++;
        }
    }
    while(r < b.size()){
        ans.push_back(b[r]);
        r++;
    }

    while(l < a.size()){
        ans.push_back(a[l]);
        l++;
    }
    return ans;
}

void merge_sort(vector<int>& a){
    if(a.size()==1){return;}
    else{
        vector<int> l,r;
        for(int i = 0 ; i < a.size()/2;i++){
            l.push_back(a[i]);
        }
        for(int i = a.size()/2;i<a.size();i++){
            r.push_back(a[i]);
        }
        merge_sort(l);
        merge_sort(r);
        a = merging(l,r);
    }

}

int main(){
    ll n;
    cin >> n;
    
    vector<int> a(n);

    REP(n){cin >> a[i];}
    
    merge_sort(a);
    for(int i = 0 ; i < n; i ++){
        cout << a[i] << ' ';
    }
}