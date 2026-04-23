#//include "../my_list/main.hpp"
#include <fstream>
#include <list>
#include <forward_list>
#include <vector>

#pragma GCC optimize("O3")

using namespace::std;

#include <random>
#include <chrono>

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


struct massive_str{
    long long int a;
    bool b;
    int c;
    string s;
};

template<typename T>
vector<float> test(T stl_list){
    unsigned int max_n = 30000;
    unsigned int min_n = 100;
    int count_ins = 50;

    vector<float> my_vector;

    for(unsigned int i = min_n; i < max_n;i+=10){
        stl_list.clear();
        for(int j = 0 ; j < i ; j ++){stl_list.push_front({rand_uns(0,100000),false,0,"1"});}
        
        ///
        auto start = get_time();
        for(int k = 0 ; k < count_ins;k++){
            stl_list.push_front({rand_uns(0,100000),false,0,"1"});
            //stl_list.pop_front();
        }

        auto finish = get_time();
        my_vector.push_back(float(finish - start)/ (float)count_ins);
    }

    return my_vector;
}

int main(){
    ofstream f("3.push_list.txt", ios::out);
    f.precision(7);

    std::list<massive_str> stl_list;
    std::forward_list<massive_str> stl_f_list;
    

    auto list_m = test(stl_list);
    auto f_list_m = test(stl_f_list);

    for(int i = 0 ; i < list_m.size();i++){
        f << fixed << list_m[i] << ' ' << f_list_m[i] << '\n';
    }
}
