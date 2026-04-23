//#include "../my_vector/main.hpp"
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <chrono>

//#pragma GCC optimize("O3")

using namespace::std;

struct massive_str{
    long long int a;
    bool b;
    int c;
    //string s;
};

double get_time()
{
    return std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::steady_clock::now().time_since_epoch()).count()/1e6;
}
int rand_uns(int min, int max)
{
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}


int main(){
    ofstream f("4.map-set.txt", ios::out);
    f.precision(7);

    std::map<int,int> mapic;
    std::set<int> setic;

    std::unordered_map<int,int> u_mapic;
    std::unordered_set<int> u_setic;

    unsigned int max_n = 30000;
    unsigned int min_n = 100;
    int count_ins = 50;

    for(int i = min_n;i<max_n;i+=10){
        setic.clear();

        for(int q = 0 ; q < i ; q ++){
            setic.insert(q);
        }

        long double summ_time = 0;
        for(int j = 0 ; j < count_ins;j++){
            auto rr = rand_uns(1,1000);
            auto start = get_time();
            setic.insert(rr);
            auto finish = get_time();
            summ_time += finish-start;
        }

        f << fixed << (float)summ_time / (float)count_ins << ' ' << 0.0000003 << '\n';

    }

}
