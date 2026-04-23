#include <iostream>

template <typename T>
struct subforwardlist {
    T data;
    subforwardlist* next;
};

template <typename T>
bool init(subforwardlist<T> **sfl){
    *sfl = NULL;

    return true;
} 	//инициализация пустого недосписка 

template <typename T>
bool push_back(subforwardlist<T> **sfl, T d){
    subforwardlist<T>* start = *sfl;
    
    if(start == NULL){
        auto temp = new subforwardlist<T>;
        temp->data = d;
        temp->next = NULL;
        *sfl = temp;
    }
    else{
        auto curr = start;
        while(curr->next){
            curr = curr->next;
        }
        auto temp = new subforwardlist<T>;
        temp->data = d;
        temp->next = NULL;
        curr->next = temp;
    }

    return true;
} 	//добавление элемента в конец недосписка

template <typename T>
int pop_back(subforwardlist<T> **sfl){
    subforwardlist* start = *sfl;
    
    if(start == NULL){
        return 0;
    }
    else{
        auto prev = start;
        auto curr = start;

        if(curr->next == NULL){
            *sfl = NULL;
            auto ans = start->data;
            delete start;
            return ans;
        }

        while(curr->next){
            prev = curr;
            curr = curr->next;
        }

        T need_data = curr->data;
        delete curr;
        prev->next = NULL;

        return need_data;
    }

    return true;
} 	//удаление элемента с конца недосписка, если пустой - возвращать 0

template <typename T>
bool push_forward(subforwardlist<T> **sfl, T d){
    subforwardlist* temp = new subforwardlist;
    temp->data = d;
    temp->next = *sfl;
    *sfl = temp;

    return 1;
} 	
//добавление элемента в начало недосписка	

template <typename T>
T pop_forward(subforwardlist<T> **sfl){
    subforwardlist* start = *sfl;
    
    if(start == NULL){
        return 0;
    }

    else{
        auto second = start ->next;
        T need_data = start->data;
        
        delete *sfl;

        *sfl = second;
        
        return need_data;
    }

    return true;
} 	//удаление элемента из начала недосписка, если пустой - возвращать 0


template <typename T>
bool push_where(subforwardlist<T> **sfl, unsigned int where, T d){
    int curr_index = 0;
    subforwardlist *curr = *sfl;

    while(curr_index < where){
        curr = curr->next;
        curr_index++;
    }

    auto forward = curr->next;
    curr->next = new subforwardlist;
    curr->next->data = d;
    curr->next->next = forward;
    
    return 1;
} //добавление элемента с порядковым номером where	

template <typename T>
T erase_where(subforwardlist<T> **sfl, unsigned int where){
    int curr_index = 0;
    subforwardlist *curr = *sfl;

    while(curr_index + 1 < where){
        curr = curr->next;
        curr_index++;
    }

    auto forward = curr->next->next;
    T need_data = curr->next->data;
    delete curr->next;
    curr->next = forward;
    
    return need_data;
}	//удаление элемента с порядковым номером where

template <typename T>
void clear(subforwardlist<T> **sfl){
    subforwardlist *curr = *sfl;

    while(curr->next){
        auto last = curr;
        curr = curr->next;
        delete last;
    }
    delete curr;

    *sfl=NULL;
}	//очистить содержимое недосписка

template <typename T>
unsigned int size(subforwardlist<T>  *sfl){
    int ans =1 ;
    
    auto start = sfl;

    if(sfl == NULL){
        return 0;
    }

    while(start->next){
        start = start->next;
        ans++;
    }

    return ans;
}	//определить размер недосписка

#include <random>
#include <chrono>
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
