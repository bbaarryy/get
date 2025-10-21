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

int main(){
    //_MM_SET_DENORMALS_ZERO_MODE(_MM_DENORMALS_ZERO_ON);
    _mm_setcsr(_mm_getcsr() | 0x8040);
    ui_float a;
    a.ui = 1;
    float c = a.f;
    while(c == 0.0){
        c = a.f;
        a.ui++;
    }
    print(a.f);
    c = a.f;
    int ans=0;
    
    while(c<=1){

        c*=2;
        ans++;
    }
    cout << ans << '\n';
}