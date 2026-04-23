#include <iostream>
#include <random>
#include <chrono>

//#pragma GCC optimize("O3")

template <typename T>
class subvector{
    public:
        subvector();
        void resize(unsigned int new_capacity);
        void push_back(T d);
        T pop_back();
        void shrink_to_fit();
        void clear();
        ~subvector();
        void insert(int& i, T x);
        void erase(int i);

        T *mas;
        unsigned int top;
        unsigned int capacity;
};

// ваш код здесь
using std::cout;
using std::endl;
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

template<typename T>
subvector<T>::subvector(){
    capacity=0;
    top = 0;
    mas = NULL;
} // инициализация пустого недовектора (top и capacity по нулям, а mas это NULL)

template<typename T>
void subvector<T>::resize(unsigned int new_capacity){
    //std::cout << "Resize" << '\n';
    T* new_arr = new T[new_capacity];

    T* curr_info = mas;
    for(auto i = 0 ; i < std::min(new_capacity, capacity);i++){
        new_arr[i] = curr_info[i];
    }
    
    delete[] mas;
    mas = new_arr;
    capacity = new_capacity;
    top = std::min(top,capacity);
} 
// увеличить емкость недовектора (можно использовать и для уменьшения - тогда, 
// в рамках данной реализации, если top меньше новой capacity, то копируем только то, что влезает, и уменьшаем top до capacity)

template<typename T>
void subvector<T>::push_back(T d){
    if(capacity == top){
        (*this).resize(capacity + capacity + 10);
    }

    top++;
    mas[top-1] = d;
} // добавление элемента в конец недовектора с выделением дополнительной памяти при необходимости

template<typename T>
void subvector<T>::insert(int& ind,T x){
    if(capacity == top){
        (*this).resize(capacity + capacity + 10);
    }

    top++;
    for(int i = top ; i > ind ;i--){
        (*this).mas[i] = (*this).mas[i-1]; 
    }
    (*this).mas[ind] = x;
}

template<typename T>
void subvector<T>::erase(int ind){
    for(int w = ind ; w < top-1 ; w++){
        (*this).mas[w] = (*this).mas[w+1]; 
    }

    top--;
}

template<typename T>
T subvector<T>::pop_back(){
    if(top == 0){return {0,0,0};}

    auto ans = mas[top-1];
    top--;
    return ans;
} // удаление элемента с конца недовектора, значение удаленного элемента вернуть (если недовектор пустой, вернуть ноль)

template<typename T>
void subvector<T>::shrink_to_fit(){
    (*this).resize(top);
} // очистить неиспользуемую память, переехав на новое место с уменьшением capacity до top

template<typename T>
void subvector<T>::clear(){
    top = 0;
} // очистить содержимое недовектора, занимаемое место при этом не меняется

template<typename T>
subvector<T>::~subvector(){
    top=0;
    capacity = 0;
    delete[] mas;
}	// очистить всю используемую память, инициализировать недовектор как пустой
