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
    unsigned int a;
    float b;
};

void print(float y){
    ui_float ans;
    ans.b = y;
    string s = bin_ui(ans.a);
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
    cout.precision(10);
    //y = x^2
    ofstream f("integrate_double.txt", ios::out);

    for(double q = 10; q <= 1e8;q+=600){
        double delta = 1/q;
        double x = 0;
        double ans = 0;

        while (x < 1){
            ans += delta * x * x;
            x += delta;
        }

        f << fixed << ans << '\n';
    }
}