#ifndef POINT_
#define POINT_

class Point {
    int x, y;
public:
    Point();
    Point(int, int);

    int get_x();
    int get_y();
    void set_x(int);
    void set_y(int);

    void inc_x();
    void dec_x();
    void inc_y();
    void dec_y();
};

#endif
