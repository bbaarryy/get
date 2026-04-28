#include "Profiler_linux.hpp"

#include <iostream>
#include <fstream>
#include <array>

using std::array;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::fstream;


int main()
{
    Profiler_linux p;
    bool file_exist = static_cast<bool>(std::ifstream("Log.txt"));
    if (file_exist)
        std::remove("Log.txt");
    
    Profiler::Result res = p.SwitchModes();
    cout << "\nProcessor ticks per round: " << res.round_ticks << endl;
    cout << "Turns: " << res.turns << endl;
    return 0;
}