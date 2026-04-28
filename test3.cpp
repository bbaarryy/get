#include <iostream>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <thread>
#include <random>

using std::string;
using std::ostream;
using std::istream;

int main(){
    auto ttime =std::chrono::steady_clock::now();
    std::cout << ttime.time_since_epoch().count() << '\n';
    std::mt19937 rnd3(ttime.time_since_epoch().count());
}