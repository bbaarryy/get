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

void insertion(int arr[10000],int l){
    for (int i = 1; i < l; i++){
        for (int j = i; j > 0 && arr[j - 1] > arr[j]; j--){
            swap(arr[j-1],arr[j]);
        }
    }
    // REP(l){cout << arr[i] << ' ';}
    // cout << '\n';
    return;
}

int main(){
    ofstream f("o3.txt", ios::out);
    
    int arr[10000];

    for(int length = 1; length <= 4000;length ++){
        for(int i = 0 ; i < length;i++){
            arr[i] = rand_uns(-1000000,1000000);
        }
        auto start = std::chrono::high_resolution_clock::now();
        
        insertion(arr,length);
            

        auto end = std::chrono::high_resolution_clock::now();
        auto nsec = end - start;
        f << nsec.count() << endl; // работаете как с привычным cout
        
    }
}