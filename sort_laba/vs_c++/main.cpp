#pragma GCC optimize("O3")

#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <chrono>
#include <ctime>
#include <random>

int rand_uns(int min, int max){
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}

#define ll long long
#define REP(n) for(int i = 0 ; i < n ; i ++)
using namespace std;

template <typename T>
istream& operator>>(istream & in, vector<T>&a)
{
	for (auto& i : a)
		in >> i;
	return in;
}

template <typename T>
ostream& operator<< (ostream& out, const vector<T>& a) {
	for (auto& i : a) { out << i << ' '; }
	return out;
}

vector<int> merging(vector<int>& a,vector<int>& b){
    vector<int> ans;
    int l = 0,r=0;
    while(l < a.size() && r < b.size()){
        if(a[l] < b[r]){
            ans.push_back(a[l]);
            l++;
        }
        else{
            ans.push_back(b[r]);
            r++;
        }
    }
    while(r < b.size()){
        ans.push_back(b[r]);
        r++;
    }

    while(l < a.size()){
        ans.push_back(a[l]);
        l++;
    }
    return ans;
}
void merge_sort(vector<int>& a){
    if(a.size()==1){return;}
    else{
        vector<int> l,r;
        for(int i = 0 ; i < a.size()/2;i++){
            l.push_back(a[i]);
        }
        for(int i = a.size()/2;i<a.size();i++){
            r.push_back(a[i]);
        }
        merge_sort(l);
        merge_sort(r);
        a = merging(l,r);
    }

}


void insert(vector<int>& arr, int& new_num) {//добавление нового элемента
	if (arr.size() == 0) {
		arr.push_back(new_num);
	}
	else {
		arr.push_back(new_num);
		int ind = arr.size() - 1;
		// ищем место для нового элемента в структуре
		// элемент «всплывает» пока он меньше очередного родителя

		while (ind >= 0) {
			int par_ind = (ind - 1) / 2;
			if (par_ind >= 0 && arr[ind] < arr[par_ind]) {
				swap(arr[ind], arr[par_ind]);
				ind = par_ind;
			}
			else break;
		}
	}
}
void deleteNode(vector<int>& array) {
	swap(array[0], array[array.size() - 1]);//Меняем вершину коорую нужно удалить(т.е. корень) с конечным элементом
	array.pop_back();
	ll ind = 0;
	// ищем «правильное» место в структуре для элемента,
	// находящегося на вершине кучи,
	// элемент «топится» пока он больше очередного потомка
	// повторяем пока индекс элемента i меньше размера массива
	while (ind < array.size()) {
		ll child = ind * 2 + 1;
		// индекс правого потомка child+1
		// должен быть меньше размера массива
		// если значение правого потомка меньше левого,
		// то перемещаем индекс на правого потомка
		if (child + 1 < array.size() && array[child + 1] < array[child]) { child++; }
		if (child < array.size() && array[child] < array[ind]) {
			swap(array[child], array[ind]);
			ind = child;
		}
		else { break; }
	}
}
void heap_sort(vector<int>& arr){
    vector<int> heap;
    for(int i = 0 ; i < arr.size();i++){
        insert(heap,arr[i]);}
    
    vector<int> ans;
    for(int i = 0;i<arr.size();i++){
        ans.push_back(heap[0]);
        deleteNode(heap);
    }
    
    for(int i = 1 ; i < ans.size();i++){
        if(ans[i] < ans[i-1]){cout << "!" << '\n';break;}
    }
    //cout << ans << '\n';
}

void quick_sort(vector<int>& arr,int l_b,int r_b) {
    
    if(arr.size()<=1 || l_b>=r_b){return;}

    int l=l_b,r=r_b;
    int m = arr[(l+r)/2];

    while(l<r){
        while(arr[l] < m){
            l++;
        }
        while(arr[r] > m){
            r--;
        }
        if(l<=r){
            swap(arr[l], arr[r]);
            l++;r--;
        }
    }
    quick_sort(arr,l,r_b);
    quick_sort(arr,l_b,r);
}

void bubble_sort(vector<int>& arr){
    for(int i = 0; i < arr.size(); i++){
        for(int j = 0; j< arr.size()-i-1; j++){
            if(arr[j] > arr[j+1])swap(arr[j],arr[j+1]);
        }
    }
    // REP(l){cout << arr[i] << ' ';}
    // cout << '\n';
    return;
}

void print_data(string s,int ch){
    ofstream f(s, ios::out);
    
    vector<int> arr;

    for(int length = 1; length <= 5000;length ++){
        for(int i = 0 ; i < length;i++){
            if(i < arr.size()){
            arr[i] = (rand_uns(-1000,1000));}
            else{
                arr.push_back(rand_uns(-1000,1000));
            }
        }
        if (ch == 0){
            auto start = std::chrono::high_resolution_clock::now();
            sort(arr.begin(), arr.end());
            auto end = std::chrono::high_resolution_clock::now();
            auto nsec = end - start;
            f << nsec.count() << endl;
        }
        else if(ch == 1){
            auto start = std::chrono::high_resolution_clock::now();
            merge_sort(arr);
            auto end = std::chrono::high_resolution_clock::now();
            auto nsec = end - start;
            f << nsec.count() << endl;
        }
        else{
            auto start = std::chrono::high_resolution_clock::now();
            bubble_sort(arr);
            auto end = std::chrono::high_resolution_clock::now();
            auto nsec = end - start;
            f << nsec.count() << endl;
        }
    }
}


int main(){
    //print_data("data_c_merge_fast.txt", 1);
    print_data("data_bubble.txt", 2);
    return 0;
}