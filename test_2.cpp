#include <iostream>

using namespace std;

struct person{
    int a;
    int b;
};

int main(){
   
    auto a = new int[5];

    cout << a[-1] << '\n';

}