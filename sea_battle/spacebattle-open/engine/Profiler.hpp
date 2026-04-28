#ifndef PROFILER
#define PROFILER

#include"Field.hpp"

class Profiler {
public:
    struct Result
    {
        int round_ticks;
        int turns;
    };
    Result SwitchModes();
protected:
    virtual void Log(Field& field) = 0;
    virtual void PrintField(const Field& field) = 0;
    void PrintResult(Result res);
    virtual void drop();

    virtual Result PShootsB();
    virtual Result BShootsP();
    virtual Result PShootsP();
    virtual Result BShootsB();
};

#endif 
