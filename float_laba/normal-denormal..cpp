#include <xmmintrin.h>
#include <immintrin.h>
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

string bin_ui(unsigned int& a){
    int index = 0;
    string ans = "";
    while(index < 32){
        if((a & (1<<index)) != 0) ans = "1" + ans;
        else ans = "0" + ans;
        index++;
    }
    return ans;
}

union ui_float{
    unsigned int ui;
    float f;
};

void print(float y){
    ui_float ans;
    ans.f = y;
    string s = bin_ui(ans.ui);
    //cout << s << '\n';
    cout << s[0] << ' ';
    int ind = 1;
    REP(8){
        cout << s[ind];
        ind++;
    }
    cout << ' ';
    REP(23){
        cout << s[ind];
        ind++;
    }
}

void solve(ll n){
    REP(n){
        float a = 1234567.7654321;
        REP(n){
            a = a/3.1415926535;
            a = a-0.999*a;
            a = -a;
            float c = -a;
            c += 0.00001;
            float d = c+a;
            d /= 1000;
            d += a;
        }
    }
}

int main(){
    //_MM_SET_DENORMALS_ZERO_MODE(_MM_DENORMALS_ZERO_ON);
    _mm_setcsr(_mm_getcsr() | 0x8040);
    
    ofstream f("denorm.txt", ios::out);

    for(float q = 1e5; q <= 1e6;q+=300){
        auto start = std::chrono::high_resolution_clock::now();
        float delta = 1/q;
        float x = 0;
        float ans = 0;
        //print(delta);cout << '\r';
        while (x < 1){
            ans += delta * x * x;
            x += delta;
        }
        auto end = std::chrono::high_resolution_clock::now();
        auto nsec = end - start;
        f << nsec.count() << endl;
    }
}