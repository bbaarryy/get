#include "../my_vector/main.hpp"
#include <fstream>

//#pragma GCC optimize("O3")

using namespace::std;

struct massive_str{
    long long int a;
    bool b;
    int c;
    //string s;
};

int main(){
    ofstream f("1.insert.txt", ios::out);
    f.precision(7);

    /*subvector sv;
    int n = 1000;
    for(int i = 0 ; i < n ;i++){
        sv.push_back(i);
        f << sv.capacity << ' ' << sv.top << '\n';
    }*/

    ///CHECK INSERT FUNCTION
    /*
    subvector sv;
    while(1){
        int ch;
        cin >> ch;
        if(ch == 1){
            //push_back
            int x;cin >> x;
            sv.push_back(x);
        }
        else if(ch==2){
            //insert
            int i,x; cin >> i >> x;
            sv.insert(i,x);
        }
        cout << "Massive: ";
        for(int i = 0; i < sv.top;i++){
            cout << sv.mas[i] << ' ';
        }
        cout << '\n';
    }*/

    unsigned int max_n = 30000;
    unsigned int min_n = 10;
    int count_ins = 50;

    subvector<massive_str> sv;
    std::vector<massive_str> bv;

    for(unsigned int i = min_n; i < max_n;i+=10){
        sv.resize(0);
        for(int j = 0 ; j < i ; j ++){sv.push_back({rand_uns(0,100000),false,0});}
        bv.resize(0);
        for(int j = 0 ; j < i ; j ++){bv.push_back({rand_uns(0,100000),false,0});}

        ///
        auto start = get_time();
        for(int k = 0 ; k < count_ins;k++){
            int rr = rand_uns(0,sv.top);

            sv.insert(rr,{k,false,0});
            sv.pop_back();

            //sv.erase(rr);
            //sv.push_back({rand_uns(0,100000),false,0,"1"});
        }
        auto finish = get_time();
        f << fixed << float(finish - start)/ (float)count_ins << ' ';
        ///

        start = get_time();
        for (int k = 0; k < count_ins; k++){
            auto rr = rand_uns(0,i-1);

            bv.insert(bv.begin() + rr,{k,0,0});
            bv.pop_back();

            //bv.erase(bv.begin() + rr);
            //bv.push_back({rand_uns(0,100000),false,0,"1"});
        }
        finish = get_time();
        f << fixed << float(finish - start) / (float)count_ins;

        f << '\n';
    }

    cout << "Complete!" << '\n';
}
