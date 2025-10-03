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


void shaker(int arr[10000],int sz){
    int l = 0;
    int r = sz-1;
    bool flag = 0;
    while(r-l > 1){
        flag = 0;
        for (int i = l; i < r; i++){
            if(arr[i] > arr[i+1]){
                swap(arr[i],arr[i+1]);
                flag = 1;
            }
        }
        r--;
        for(int i =r;i>l;i--){
            if(arr[i] < arr[i-1]){
                swap(arr[i],arr[i-1]);
                flag = 1;
            }
        }
        if(!flag){break;}
        l++;
    }

    // REP(sz){cout << arr[i] << ' ';}
    // cout << '\n';
    return;
}

void bubble(int arr[10000],int l){
    for(int i = 0; i < l; i++){
        for(int j = 0; j< l-i-1; j++){
            if(arr[j] > arr[j+1])swap(arr[j],arr[j+1]);
        }
    }
    // REP(l){cout << arr[i] << ' ';}
    // cout << '\n';
    return;
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

void print_data(string s,int ch){
    ofstream f(s, ios::out);
    
    int arr[10000];

    for(int length = 1; length <= 4000;length ++){
        for(int i = 0 ; i < length;i++){
            arr[i] = rand_uns(-1000000,1000000);
        }
        auto start = std::chrono::high_resolution_clock::now();
        
        switch (ch)
        {
        case 0:
            shaker(arr,length);
            break;
        case 1:
            bubble(arr,length);
            break;
        case 2:
            insertion(arr,length);
            break;
        default:
            break;
        }

        auto end = std::chrono::high_resolution_clock::now();
        auto nsec = end - start;
        f << nsec.count() << endl; // работаете как с привычным cout
    }
}

void best_data(string s,int ch){
    ofstream f(s, ios::out);
    
    int arr[10000];

    for(int length = 1; length <= 4000;length ++){
        for(int i = 0 ; i < length;i++){
            arr[i] = i;
        }
        auto start = std::chrono::high_resolution_clock::now();
        
        switch (ch)
        {
        case 0:
            shaker(arr,length);
            break;
        case 1:
            bubble(arr,length);
            break;
        case 2:
            insertion(arr,length);
            break;
        default:
            break;
        }

        auto end = std::chrono::high_resolution_clock::now();
        auto nsec = end - start;
        f << nsec.count() << endl; // работаете как с привычным cout
    }
}

void worst_data(string s,int ch){
    ofstream f(s, ios::out);
    
    int arr[10000];

    for(int length = 1; length <= 4000;length ++){
        for(int i = 0 ; i < length;i++){
            arr[i] = length-i;
        }
        auto start = std::chrono::high_resolution_clock::now();
        
        switch (ch)
        {
        case 0:
            shaker(arr,length);
            break;
        case 1:
            bubble(arr,length);
            break;
        case 2:
            insertion(arr,length);
            break;
        default:
            break;
        }

        auto end = std::chrono::high_resolution_clock::now();
        auto nsec = end - start;
        f << nsec.count() << endl; // работаете как с привычным cout
    }
}

int main(){

    print_data("data_shaker_b.txt", 0);
    print_data("data_bubble_b.txt",2);
    print_data("data_insertion_b.txt",1);

    // best_data("data_shaker_b.txt", 0);
    // best_data("data_bubble_b.txt",2);
    // best_data("data_insertion_b.txt",1);

    // worst_data("data_shaker_w.txt", 0);
    // worst_data("data_bubble_w.txt",1);
    // worst_data("data_insertion_w.txt",2);

    
    return 0;
}