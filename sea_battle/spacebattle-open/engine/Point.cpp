#include "Point.hpp"


Point::Point() : Point(0, 0) {}

Point::Point(int x, int y) : x(x), y(y) {}

int Point::get_x()
{
    return x;
}

int Point::get_y()
{
    return y;
}

void Point::set_x(int _x)
{
    x = _x;
}

void Point::set_y(int _y)
{
    y = _y;
}


void Point::inc_x()
{
    x++;
}

void Point::dec_x()
{
    x--;
}


void Point::inc_y()
{
    y++;
}

void Point::dec_y()
{
    y--;
}