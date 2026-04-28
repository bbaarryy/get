#ifndef FIELD
#define FIELD

#include "TypesAndConsts.hpp"
#include <array>

using std::array;

class Field {
private:
    array< array<char, FIELD_SIZE>, FIELD_SIZE> data; // storing the field
public:
    Field& operator=(const Field& src);
    array<char, FIELD_SIZE>& operator[](int i);
    const array<char, FIELD_SIZE>& operator[](int i) const;
};

#endif