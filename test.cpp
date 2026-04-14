#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;

struct wr{
    int day,id,ca,o2_air,co2_air,k,ph;
};

bool comp(wr& a,wr& b){
    return a.day < b.day;
}

int main(){
    int n;cin>>n;
    std::vector<wr> arr;
    for(int i = 0 ; i < n ;i++){
        int day,id,ca,o2_air,co2_air,k,ph;
        cin >> day>>id>>ca>>o2_air>>co2_air>>k>>ph;
        arr.push_back({day,id,ca,o2_air,co2_air,k,ph});
    }
    sort(arr.begin(),arr.end(),comp);

    int curr_ans= 0;
    int ans = -1000;
    for(int i = 1 ; i < arr.size();i++){
        if(arr[i].day - arr[i].day == 1){
            if(arr[i].ca >= arr[i-1].ca && arr[i].co2_air < arr[i-1].co2_air){
                curr_ans++;
                ans = std::max(curr_ans,ans);
            }
            else curr_ans=0;
        }
        else curr_ans = 0;
    }
    ans = std::max(curr_ans,ans);
    cout << ans << '\n';
}