#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;

int main(){
    int* arr = new int[10];
    for (int i = 0 ; i < 10 ; i ++){
        arr[i] = i;
    }
    cout << arr[5] << '\n';

    delete[] arr;

    return 0;
}