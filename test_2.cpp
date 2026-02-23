#include <iostream>

using std::cout;
using std::cin;

class Animal {
public:
    // Погладить данную зверушку.
    // Последствия зависят от реализации данного метода для класса конкретной зверушки.
    virtual void pet() = 0;

    virtual ~Animal() {};
};

//У вас есть интерфейс NPC. Вот такой:

class NPC {
public:
    // Поговорить с NPC.
    // Что он скажет - зависит от реализации данного метода для конкретного NPC.
    virtual void talk() = 0;

    virtual ~NPC() {};
};

class SmartCat : public NPC, public Animal{
public:
    void talk(){
        cout << "Meow\n";
    }
    void pet(){
        cout << "Meow\n";
    }
};

int main() {
    
}
