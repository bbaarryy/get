#pragma GCC optimize("O3")

#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <chrono>
#include <ctime>
#include <random>

int rand_uns(int min, int max){
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}

#define ll long long
#define REP(n) for(int i = 0 ; i < n ; i ++)
using namespace std;

template <typename T>
istream& operator>>(istream & in, vector<T>&a)
{
	for (auto& i : a)
		in >> i;
	return in;
}

template <typename T>
ostream& operator<< (ostream& out, const vector<T>& a) {
	for (auto& i : a) { out << i << ' '; }
	return out;
}

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
    ofstream f("olog3.txt", ios::out);
    
    vector<int> arr;

    for(int length = 1; length <= 4000;length ++){
        for(int i = 0 ; i < length;i++){
            if(i>=arr.size()){
                arr.push_back(rand_uns(-1000000,1000000));
            }
            else{arr[i] = rand_uns(-1000000,1000000);}
        }
        auto start = std::chrono::high_resolution_clock::now();
        
        merge_sort(arr);
            

        auto end = std::chrono::high_resolution_clock::now();
        auto nsec = end - start;
        f << nsec.count() << endl; // работаете как с привычным cout
        
    }
}