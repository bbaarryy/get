#include "Field.hpp"

Field& Field::operator=(const Field& src)
{
    data = src.data;
    return *this;
}

array<char, FIELD_SIZE>& Field::operator[](int i)
{
    return data[i];
}

const array<char, FIELD_SIZE>& Field::operator[](int i) const
{
    return data[i];
}